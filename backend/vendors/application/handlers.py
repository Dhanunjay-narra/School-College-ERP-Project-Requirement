"""
Vendor Management & Compliance — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for vendors.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.vendors.domain.entities import VendorsEntity
from backend.vendors.domain.repositories import IVendorsRepository
from backend.vendors.domain.events import VendorsCreatedEvent, VendorsUpdatedEvent
from backend.vendors.application.commands import CreateVendorsCommand, UpdateVendorsCommand, DeleteVendorsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.vendors.handlers")

class VendorsCommandHandler:
    def __init__(self, repository: IVendorsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateVendorsCommand) -> VendorsEntity:
        logger.info(f"Handling CreateVendorsCommand: {cmd.code}")
        entity = VendorsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(VendorsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateVendorsCommand) -> VendorsEntity:
        logger.info(f"Handling UpdateVendorsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Vendors", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(VendorsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteVendorsCommand) -> bool:
        logger.info(f"Handling DeleteVendorsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for vendors."""
    logger.info(f"Received domain event in vendors: {event.event_type} (Aggregate: {event.aggregate_id})")
