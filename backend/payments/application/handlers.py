"""
Payment Abstraction Gateway — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for payments.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.payments.domain.entities import PaymentsEntity
from backend.payments.domain.repositories import IPaymentsRepository
from backend.payments.domain.events import PaymentsCreatedEvent, PaymentsUpdatedEvent
from backend.payments.application.commands import CreatePaymentsCommand, UpdatePaymentsCommand, DeletePaymentsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.payments.handlers")

class PaymentsCommandHandler:
    def __init__(self, repository: IPaymentsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreatePaymentsCommand) -> PaymentsEntity:
        logger.info(f"Handling CreatePaymentsCommand: {cmd.code}")
        entity = PaymentsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(PaymentsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdatePaymentsCommand) -> PaymentsEntity:
        logger.info(f"Handling UpdatePaymentsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Payments", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(PaymentsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeletePaymentsCommand) -> bool:
        logger.info(f"Handling DeletePaymentsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for payments."""
    logger.info(f"Received domain event in payments: {event.event_type} (Aggregate: {event.aggregate_id})")
