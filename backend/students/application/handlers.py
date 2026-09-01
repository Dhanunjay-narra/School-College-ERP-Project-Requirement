"""
Student Information & Lifecycle — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for students.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.students.domain.entities import StudentsEntity
from backend.students.domain.repositories import IStudentsRepository
from backend.students.domain.events import StudentsCreatedEvent, StudentsUpdatedEvent
from backend.students.application.commands import CreateStudentsCommand, UpdateStudentsCommand, DeleteStudentsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.students.handlers")

class StudentsCommandHandler:
    def __init__(self, repository: IStudentsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateStudentsCommand) -> StudentsEntity:
        logger.info(f"Handling CreateStudentsCommand: {cmd.code}")
        entity = StudentsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(StudentsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateStudentsCommand) -> StudentsEntity:
        logger.info(f"Handling UpdateStudentsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Students", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(StudentsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteStudentsCommand) -> bool:
        logger.info(f"Handling DeleteStudentsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for students."""
    logger.info(f"Received domain event in students: {event.event_type} (Aggregate: {event.aggregate_id})")
