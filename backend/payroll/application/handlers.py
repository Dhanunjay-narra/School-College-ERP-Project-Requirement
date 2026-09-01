"""
Integrated Payroll Engine — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for payroll.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.payroll.domain.entities import PayrollEntity
from backend.payroll.domain.repositories import IPayrollRepository
from backend.payroll.domain.events import PayrollCreatedEvent, PayrollUpdatedEvent
from backend.payroll.application.commands import CreatePayrollCommand, UpdatePayrollCommand, DeletePayrollCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.payroll.handlers")

class PayrollCommandHandler:
    def __init__(self, repository: IPayrollRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreatePayrollCommand) -> PayrollEntity:
        logger.info(f"Handling CreatePayrollCommand: {cmd.code}")
        entity = PayrollEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(PayrollCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdatePayrollCommand) -> PayrollEntity:
        logger.info(f"Handling UpdatePayrollCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Payroll", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(PayrollUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeletePayrollCommand) -> bool:
        logger.info(f"Handling DeletePayrollCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for payroll."""
    logger.info(f"Received domain event in payroll: {event.event_type} (Aggregate: {event.aggregate_id})")
