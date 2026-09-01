"""
Campus Store & Cafeteria POS — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for campus_store.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.campus_store.domain.entities import CampusStoreEntity
from backend.campus_store.domain.repositories import ICampusStoreRepository
from backend.campus_store.domain.events import CampusStoreCreatedEvent, CampusStoreUpdatedEvent
from backend.campus_store.application.commands import CreateCampusStoreCommand, UpdateCampusStoreCommand, DeleteCampusStoreCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.campus_store.handlers")

class CampusStoreCommandHandler:
    def __init__(self, repository: ICampusStoreRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateCampusStoreCommand) -> CampusStoreEntity:
        logger.info(f"Handling CreateCampusStoreCommand: {cmd.code}")
        entity = CampusStoreEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(CampusStoreCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateCampusStoreCommand) -> CampusStoreEntity:
        logger.info(f"Handling UpdateCampusStoreCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("CampusStore", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(CampusStoreUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteCampusStoreCommand) -> bool:
        logger.info(f"Handling DeleteCampusStoreCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for campus_store."""
    logger.info(f"Received domain event in campus_store: {event.event_type} (Aggregate: {event.aggregate_id})")
