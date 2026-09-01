"""
Asset Lifecycle & Depreciation — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for assets.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.assets.domain.entities import AssetsEntity
from backend.assets.domain.repositories import IAssetsRepository
from backend.assets.domain.events import AssetsCreatedEvent, AssetsUpdatedEvent
from backend.assets.application.commands import CreateAssetsCommand, UpdateAssetsCommand, DeleteAssetsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.assets.handlers")

class AssetsCommandHandler:
    def __init__(self, repository: IAssetsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateAssetsCommand) -> AssetsEntity:
        logger.info(f"Handling CreateAssetsCommand: {cmd.code}")
        entity = AssetsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(AssetsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateAssetsCommand) -> AssetsEntity:
        logger.info(f"Handling UpdateAssetsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Assets", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(AssetsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteAssetsCommand) -> bool:
        logger.info(f"Handling DeleteAssetsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for assets."""
    logger.info(f"Received domain event in assets: {event.event_type} (Aggregate: {event.aggregate_id})")
