"""
Identity & Access Management — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for identity.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.identity.domain.entities import IdentityEntity
from backend.identity.domain.repositories import IIdentityRepository
from backend.identity.domain.events import IdentityCreatedEvent, IdentityUpdatedEvent
from backend.identity.application.commands import CreateIdentityCommand, UpdateIdentityCommand, DeleteIdentityCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.identity.handlers")

class IdentityCommandHandler:
    def __init__(self, repository: IIdentityRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateIdentityCommand) -> IdentityEntity:
        logger.info(f"Handling CreateIdentityCommand: {cmd.code}")
        entity = IdentityEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(IdentityCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateIdentityCommand) -> IdentityEntity:
        logger.info(f"Handling UpdateIdentityCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Identity", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(IdentityUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteIdentityCommand) -> bool:
        logger.info(f"Handling DeleteIdentityCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for identity."""
    logger.info(f"Received domain event in identity: {event.event_type} (Aggregate: {event.aggregate_id})")
