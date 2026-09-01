"""
Hostel & Housing Management — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for hostels.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.hostels.domain.entities import HostelsEntity
from backend.hostels.domain.repositories import IHostelsRepository
from backend.hostels.domain.events import HostelsCreatedEvent, HostelsUpdatedEvent
from backend.hostels.application.commands import CreateHostelsCommand, UpdateHostelsCommand, DeleteHostelsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.hostels.handlers")

class HostelsCommandHandler:
    def __init__(self, repository: IHostelsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateHostelsCommand) -> HostelsEntity:
        logger.info(f"Handling CreateHostelsCommand: {cmd.code}")
        entity = HostelsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(HostelsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateHostelsCommand) -> HostelsEntity:
        logger.info(f"Handling UpdateHostelsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Hostels", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(HostelsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteHostelsCommand) -> bool:
        logger.info(f"Handling DeleteHostelsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for hostels."""
    logger.info(f"Received domain event in hostels: {event.event_type} (Aggregate: {event.aggregate_id})")
