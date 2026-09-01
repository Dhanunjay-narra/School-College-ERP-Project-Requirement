"""
Smart Attendance Engine — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for attendance.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.attendance.domain.entities import AttendanceEntity
from backend.attendance.domain.repositories import IAttendanceRepository
from backend.attendance.domain.events import AttendanceCreatedEvent, AttendanceUpdatedEvent
from backend.attendance.application.commands import CreateAttendanceCommand, UpdateAttendanceCommand, DeleteAttendanceCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.attendance.handlers")

class AttendanceCommandHandler:
    def __init__(self, repository: IAttendanceRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateAttendanceCommand) -> AttendanceEntity:
        logger.info(f"Handling CreateAttendanceCommand: {cmd.code}")
        entity = AttendanceEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(AttendanceCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateAttendanceCommand) -> AttendanceEntity:
        logger.info(f"Handling UpdateAttendanceCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Attendance", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(AttendanceUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteAttendanceCommand) -> bool:
        logger.info(f"Handling DeleteAttendanceCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for attendance."""
    logger.info(f"Received domain event in attendance: {event.event_type} (Aggregate: {event.aggregate_id})")
