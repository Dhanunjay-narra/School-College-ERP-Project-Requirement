"""
Alumni Network & Relations — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for alumni.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.alumni.domain.entities import AlumniEntity
from backend.alumni.domain.repositories import IAlumniRepository
from backend.alumni.domain.events import AlumniCreatedEvent, AlumniUpdatedEvent
from backend.alumni.application.commands import CreateAlumniCommand, UpdateAlumniCommand, DeleteAlumniCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.alumni.handlers")

class AlumniCommandHandler:
    def __init__(self, repository: IAlumniRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateAlumniCommand) -> AlumniEntity:
        logger.info(f"Handling CreateAlumniCommand: {cmd.code}")
        entity = AlumniEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(AlumniCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateAlumniCommand) -> AlumniEntity:
        logger.info(f"Handling UpdateAlumniCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Alumni", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(AlumniUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteAlumniCommand) -> bool:
        logger.info(f"Handling DeleteAlumniCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for alumni."""
    logger.info(f"Received domain event in alumni: {event.event_type} (Aggregate: {event.aggregate_id})")
