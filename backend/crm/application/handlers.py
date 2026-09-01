"""
Institutional CRM & Admissions Leads — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for crm.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.crm.domain.entities import CrmEntity
from backend.crm.domain.repositories import ICrmRepository
from backend.crm.domain.events import CrmCreatedEvent, CrmUpdatedEvent
from backend.crm.application.commands import CreateCrmCommand, UpdateCrmCommand, DeleteCrmCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.crm.handlers")

class CrmCommandHandler:
    def __init__(self, repository: ICrmRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateCrmCommand) -> CrmEntity:
        logger.info(f"Handling CreateCrmCommand: {cmd.code}")
        entity = CrmEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(CrmCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateCrmCommand) -> CrmEntity:
        logger.info(f"Handling UpdateCrmCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Crm", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(CrmUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteCrmCommand) -> bool:
        logger.info(f"Handling DeleteCrmCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for crm."""
    logger.info(f"Received domain event in crm: {event.event_type} (Aggregate: {event.aggregate_id})")
