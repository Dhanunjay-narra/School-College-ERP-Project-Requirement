"""
Faculty & Workload Management — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for faculty.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.faculty.domain.entities import FacultyEntity
from backend.faculty.domain.repositories import IFacultyRepository
from backend.faculty.domain.events import FacultyCreatedEvent, FacultyUpdatedEvent
from backend.faculty.application.commands import CreateFacultyCommand, UpdateFacultyCommand, DeleteFacultyCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.faculty.handlers")

class FacultyCommandHandler:
    def __init__(self, repository: IFacultyRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateFacultyCommand) -> FacultyEntity:
        logger.info(f"Handling CreateFacultyCommand: {cmd.code}")
        entity = FacultyEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(FacultyCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateFacultyCommand) -> FacultyEntity:
        logger.info(f"Handling UpdateFacultyCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Faculty", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(FacultyUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteFacultyCommand) -> bool:
        logger.info(f"Handling DeleteFacultyCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for faculty."""
    logger.info(f"Received domain event in faculty: {event.event_type} (Aggregate: {event.aggregate_id})")
