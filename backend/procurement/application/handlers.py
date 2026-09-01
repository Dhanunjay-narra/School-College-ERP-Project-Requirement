"""
Procurement Management — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for procurement.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.procurement.domain.entities import ProcurementEntity
from backend.procurement.domain.repositories import IProcurementRepository
from backend.procurement.domain.events import ProcurementCreatedEvent, ProcurementUpdatedEvent
from backend.procurement.application.commands import CreateProcurementCommand, UpdateProcurementCommand, DeleteProcurementCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.procurement.handlers")

class ProcurementCommandHandler:
    def __init__(self, repository: IProcurementRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateProcurementCommand) -> ProcurementEntity:
        logger.info(f"Handling CreateProcurementCommand: {cmd.code}")
        entity = ProcurementEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(ProcurementCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateProcurementCommand) -> ProcurementEntity:
        logger.info(f"Handling UpdateProcurementCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Procurement", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(ProcurementUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteProcurementCommand) -> bool:
        logger.info(f"Handling DeleteProcurementCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for procurement."""
    logger.info(f"Received domain event in procurement: {event.event_type} (Aggregate: {event.aggregate_id})")
