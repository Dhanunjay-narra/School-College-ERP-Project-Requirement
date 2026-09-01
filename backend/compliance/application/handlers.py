"""
Accreditation & Regulatory Compliance — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for compliance.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.compliance.domain.entities import ComplianceEntity
from backend.compliance.domain.repositories import IComplianceRepository
from backend.compliance.domain.events import ComplianceCreatedEvent, ComplianceUpdatedEvent
from backend.compliance.application.commands import CreateComplianceCommand, UpdateComplianceCommand, DeleteComplianceCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.compliance.handlers")

class ComplianceCommandHandler:
    def __init__(self, repository: IComplianceRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateComplianceCommand) -> ComplianceEntity:
        logger.info(f"Handling CreateComplianceCommand: {cmd.code}")
        entity = ComplianceEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(ComplianceCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateComplianceCommand) -> ComplianceEntity:
        logger.info(f"Handling UpdateComplianceCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Compliance", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(ComplianceUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteComplianceCommand) -> bool:
        logger.info(f"Handling DeleteComplianceCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for compliance."""
    logger.info(f"Received domain event in compliance: {event.event_type} (Aggregate: {event.aggregate_id})")
