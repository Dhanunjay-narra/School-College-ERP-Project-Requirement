"""
LMS & Assignments — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for assignments.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.assignments.domain.entities import AssignmentsEntity
from backend.assignments.domain.repositories import IAssignmentsRepository
from backend.assignments.domain.events import AssignmentsCreatedEvent, AssignmentsUpdatedEvent
from backend.assignments.application.commands import CreateAssignmentsCommand, UpdateAssignmentsCommand, DeleteAssignmentsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.assignments.handlers")

class AssignmentsCommandHandler:
    def __init__(self, repository: IAssignmentsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateAssignmentsCommand) -> AssignmentsEntity:
        logger.info(f"Handling CreateAssignmentsCommand: {cmd.code}")
        entity = AssignmentsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(AssignmentsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateAssignmentsCommand) -> AssignmentsEntity:
        logger.info(f"Handling UpdateAssignmentsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Assignments", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(AssignmentsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteAssignmentsCommand) -> bool:
        logger.info(f"Handling DeleteAssignmentsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for assignments."""
    logger.info(f"Received domain event in assignments: {event.event_type} (Aggregate: {event.aggregate_id})")
