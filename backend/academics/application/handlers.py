"""
Academic Structure & Timetable — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for academics.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.academics.domain.entities import AcademicsEntity
from backend.academics.domain.repositories import IAcademicsRepository
from backend.academics.domain.events import AcademicsCreatedEvent, AcademicsUpdatedEvent
from backend.academics.application.commands import CreateAcademicsCommand, UpdateAcademicsCommand, DeleteAcademicsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.academics.handlers")

class AcademicsCommandHandler:
    def __init__(self, repository: IAcademicsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateAcademicsCommand) -> AcademicsEntity:
        logger.info(f"Handling CreateAcademicsCommand: {cmd.code}")
        entity = AcademicsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(AcademicsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateAcademicsCommand) -> AcademicsEntity:
        logger.info(f"Handling UpdateAcademicsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Academics", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(AcademicsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteAcademicsCommand) -> bool:
        logger.info(f"Handling DeleteAcademicsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for academics."""
    logger.info(f"Received domain event in academics: {event.event_type} (Aggregate: {event.aggregate_id})")
