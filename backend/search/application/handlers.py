"""
Centralized Faceted Search — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for search.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.search.domain.entities import SearchEntity
from backend.search.domain.repositories import ISearchRepository
from backend.search.domain.events import SearchCreatedEvent, SearchUpdatedEvent
from backend.search.application.commands import CreateSearchCommand, UpdateSearchCommand, DeleteSearchCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.search.handlers")

class SearchCommandHandler:
    def __init__(self, repository: ISearchRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateSearchCommand) -> SearchEntity:
        logger.info(f"Handling CreateSearchCommand: {cmd.code}")
        entity = SearchEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(SearchCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateSearchCommand) -> SearchEntity:
        logger.info(f"Handling UpdateSearchCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Search", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(SearchUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteSearchCommand) -> bool:
        logger.info(f"Handling DeleteSearchCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for search."""
    logger.info(f"Received domain event in search: {event.event_type} (Aggregate: {event.aggregate_id})")
