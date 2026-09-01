"""
Human Resource & Recruitment — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for hr.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.hr.domain.entities import HrEntity
from backend.hr.domain.repositories import IHrRepository
from backend.hr.domain.events import HrCreatedEvent, HrUpdatedEvent
from backend.hr.application.commands import CreateHrCommand, UpdateHrCommand, DeleteHrCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.hr.handlers")

class HrCommandHandler:
    def __init__(self, repository: IHrRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateHrCommand) -> HrEntity:
        logger.info(f"Handling CreateHrCommand: {cmd.code}")
        entity = HrEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(HrCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateHrCommand) -> HrEntity:
        logger.info(f"Handling UpdateHrCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Hr", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(HrUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteHrCommand) -> bool:
        logger.info(f"Handling DeleteHrCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for hr."""
    logger.info(f"Received domain event in hr: {event.event_type} (Aggregate: {event.aggregate_id})")
