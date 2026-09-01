"""
Finance & General Ledger — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for finance.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.finance.domain.entities import FinanceEntity
from backend.finance.domain.repositories import IFinanceRepository
from backend.finance.domain.events import FinanceCreatedEvent, FinanceUpdatedEvent
from backend.finance.application.commands import CreateFinanceCommand, UpdateFinanceCommand, DeleteFinanceCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.finance.handlers")

class FinanceCommandHandler:
    def __init__(self, repository: IFinanceRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateFinanceCommand) -> FinanceEntity:
        logger.info(f"Handling CreateFinanceCommand: {cmd.code}")
        entity = FinanceEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(FinanceCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateFinanceCommand) -> FinanceEntity:
        logger.info(f"Handling UpdateFinanceCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Finance", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(FinanceUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteFinanceCommand) -> bool:
        logger.info(f"Handling DeleteFinanceCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for finance."""
    logger.info(f"Received domain event in finance: {event.event_type} (Aggregate: {event.aggregate_id})")
