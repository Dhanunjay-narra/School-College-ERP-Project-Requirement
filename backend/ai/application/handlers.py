"""
AI/ML Predictive Intelligence — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for ai.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.ai.domain.entities import AiEntity
from backend.ai.domain.repositories import IAiRepository
from backend.ai.domain.events import AiCreatedEvent, AiUpdatedEvent
from backend.ai.application.commands import CreateAiCommand, UpdateAiCommand, DeleteAiCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.ai.handlers")

class AiCommandHandler:
    def __init__(self, repository: IAiRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateAiCommand) -> AiEntity:
        logger.info(f"Handling CreateAiCommand: {cmd.code}")
        entity = AiEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(AiCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateAiCommand) -> AiEntity:
        logger.info(f"Handling UpdateAiCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Ai", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(AiUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteAiCommand) -> bool:
        logger.info(f"Handling DeleteAiCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for ai."""
    logger.info(f"Received domain event in ai: {event.event_type} (Aggregate: {event.aggregate_id})")
