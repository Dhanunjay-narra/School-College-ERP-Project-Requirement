"""
Library & RFID Circulation — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for library.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.library.domain.entities import LibraryEntity
from backend.library.domain.repositories import ILibraryRepository
from backend.library.domain.events import LibraryCreatedEvent, LibraryUpdatedEvent
from backend.library.application.commands import CreateLibraryCommand, UpdateLibraryCommand, DeleteLibraryCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.library.handlers")

class LibraryCommandHandler:
    def __init__(self, repository: ILibraryRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateLibraryCommand) -> LibraryEntity:
        logger.info(f"Handling CreateLibraryCommand: {cmd.code}")
        entity = LibraryEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(LibraryCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateLibraryCommand) -> LibraryEntity:
        logger.info(f"Handling UpdateLibraryCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Library", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(LibraryUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteLibraryCommand) -> bool:
        logger.info(f"Handling DeleteLibraryCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for library."""
    logger.info(f"Received domain event in library: {event.event_type} (Aggregate: {event.aggregate_id})")
