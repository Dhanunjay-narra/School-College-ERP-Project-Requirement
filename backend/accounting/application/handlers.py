"""
Accounts Payable & Receivable — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for accounting.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.accounting.domain.entities import AccountingEntity
from backend.accounting.domain.repositories import IAccountingRepository
from backend.accounting.domain.events import AccountingCreatedEvent, AccountingUpdatedEvent
from backend.accounting.application.commands import CreateAccountingCommand, UpdateAccountingCommand, DeleteAccountingCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.accounting.handlers")

class AccountingCommandHandler:
    def __init__(self, repository: IAccountingRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateAccountingCommand) -> AccountingEntity:
        logger.info(f"Handling CreateAccountingCommand: {cmd.code}")
        entity = AccountingEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(AccountingCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateAccountingCommand) -> AccountingEntity:
        logger.info(f"Handling UpdateAccountingCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Accounting", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(AccountingUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteAccountingCommand) -> bool:
        logger.info(f"Handling DeleteAccountingCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for accounting."""
    logger.info(f"Received domain event in accounting: {event.event_type} (Aggregate: {event.aggregate_id})")
