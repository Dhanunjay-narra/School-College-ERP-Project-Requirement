"""
Immutable Audit Logging — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for audit.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.audit.domain.entities import AuditEntity
from backend.audit.domain.repositories import IAuditRepository
from backend.audit.domain.events import AuditCreatedEvent, AuditUpdatedEvent
from backend.audit.application.commands import CreateAuditCommand, UpdateAuditCommand, DeleteAuditCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.audit.handlers")

class AuditCommandHandler:
    def __init__(self, repository: IAuditRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateAuditCommand) -> AuditEntity:
        logger.info(f"Handling CreateAuditCommand: {cmd.code}")
        entity = AuditEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(AuditCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateAuditCommand) -> AuditEntity:
        logger.info(f"Handling UpdateAuditCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Audit", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(AuditUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteAuditCommand) -> bool:
        logger.info(f"Handling DeleteAuditCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for audit."""
    logger.info(f"Received domain event in audit: {event.event_type} (Aggregate: {event.aggregate_id})")
