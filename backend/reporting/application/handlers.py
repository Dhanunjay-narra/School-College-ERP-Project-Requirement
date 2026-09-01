"""
Universal Enterprise Reporting — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for reporting.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.reporting.domain.entities import ReportingEntity
from backend.reporting.domain.repositories import IReportingRepository
from backend.reporting.domain.events import ReportingCreatedEvent, ReportingUpdatedEvent
from backend.reporting.application.commands import CreateReportingCommand, UpdateReportingCommand, DeleteReportingCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.reporting.handlers")

class ReportingCommandHandler:
    def __init__(self, repository: IReportingRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateReportingCommand) -> ReportingEntity:
        logger.info(f"Handling CreateReportingCommand: {cmd.code}")
        entity = ReportingEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(ReportingCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateReportingCommand) -> ReportingEntity:
        logger.info(f"Handling UpdateReportingCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Reporting", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(ReportingUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteReportingCommand) -> bool:
        logger.info(f"Handling DeleteReportingCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for reporting."""
    logger.info(f"Received domain event in reporting: {event.event_type} (Aggregate: {event.aggregate_id})")
