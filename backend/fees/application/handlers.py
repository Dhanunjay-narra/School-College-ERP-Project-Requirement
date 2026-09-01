"""
Fees & Student Billing — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for fees.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.fees.domain.entities import FeesEntity
from backend.fees.domain.repositories import IFeesRepository
from backend.fees.domain.events import FeesCreatedEvent, FeesUpdatedEvent
from backend.fees.application.commands import CreateFeesCommand, UpdateFeesCommand, DeleteFeesCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.fees.handlers")

class FeesCommandHandler:
    def __init__(self, repository: IFeesRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateFeesCommand) -> FeesEntity:
        logger.info(f"Handling CreateFeesCommand: {cmd.code}")
        entity = FeesEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(FeesCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateFeesCommand) -> FeesEntity:
        logger.info(f"Handling UpdateFeesCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Fees", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(FeesUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteFeesCommand) -> bool:
        logger.info(f"Handling DeleteFeesCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for fees."""
    logger.info(f"Received domain event in fees: {event.event_type} (Aggregate: {event.aggregate_id})")
