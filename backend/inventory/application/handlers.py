"""
Campus Inventory & Stores — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for inventory.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.inventory.domain.entities import InventoryEntity
from backend.inventory.domain.repositories import IInventoryRepository
from backend.inventory.domain.events import InventoryCreatedEvent, InventoryUpdatedEvent
from backend.inventory.application.commands import CreateInventoryCommand, UpdateInventoryCommand, DeleteInventoryCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.inventory.handlers")

class InventoryCommandHandler:
    def __init__(self, repository: IInventoryRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateInventoryCommand) -> InventoryEntity:
        logger.info(f"Handling CreateInventoryCommand: {cmd.code}")
        entity = InventoryEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(InventoryCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateInventoryCommand) -> InventoryEntity:
        logger.info(f"Handling UpdateInventoryCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Inventory", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(InventoryUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteInventoryCommand) -> bool:
        logger.info(f"Handling DeleteInventoryCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for inventory."""
    logger.info(f"Received domain event in inventory: {event.event_type} (Aggregate: {event.aggregate_id})")
