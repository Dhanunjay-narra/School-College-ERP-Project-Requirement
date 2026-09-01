"""
Document Management & Signatures — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for documents.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.documents.domain.entities import DocumentsEntity
from backend.documents.domain.repositories import IDocumentsRepository
from backend.documents.domain.events import DocumentsCreatedEvent, DocumentsUpdatedEvent
from backend.documents.application.commands import CreateDocumentsCommand, UpdateDocumentsCommand, DeleteDocumentsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.documents.handlers")

class DocumentsCommandHandler:
    def __init__(self, repository: IDocumentsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateDocumentsCommand) -> DocumentsEntity:
        logger.info(f"Handling CreateDocumentsCommand: {cmd.code}")
        entity = DocumentsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(DocumentsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateDocumentsCommand) -> DocumentsEntity:
        logger.info(f"Handling UpdateDocumentsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Documents", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(DocumentsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteDocumentsCommand) -> bool:
        logger.info(f"Handling DeleteDocumentsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for documents."""
    logger.info(f"Received domain event in documents: {event.event_type} (Aggregate: {event.aggregate_id})")
