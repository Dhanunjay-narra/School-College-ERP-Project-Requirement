"""
BI & Institutional Analytics — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for analytics.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.analytics.domain.entities import AnalyticsEntity
from backend.analytics.domain.repositories import IAnalyticsRepository
from backend.analytics.domain.events import AnalyticsCreatedEvent, AnalyticsUpdatedEvent
from backend.analytics.application.commands import CreateAnalyticsCommand, UpdateAnalyticsCommand, DeleteAnalyticsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.analytics.handlers")

class AnalyticsCommandHandler:
    def __init__(self, repository: IAnalyticsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateAnalyticsCommand) -> AnalyticsEntity:
        logger.info(f"Handling CreateAnalyticsCommand: {cmd.code}")
        entity = AnalyticsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(AnalyticsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateAnalyticsCommand) -> AnalyticsEntity:
        logger.info(f"Handling UpdateAnalyticsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Analytics", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(AnalyticsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteAnalyticsCommand) -> bool:
        logger.info(f"Handling DeleteAnalyticsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for analytics."""
    logger.info(f"Received domain event in analytics: {event.event_type} (Aggregate: {event.aggregate_id})")
