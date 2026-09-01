"""
Universal Multi-Channel Notifications — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for communication.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.communication.domain.entities import CommunicationEntity
from backend.communication.domain.repositories import ICommunicationRepository
from backend.communication.domain.events import CommunicationCreatedEvent, CommunicationUpdatedEvent
from backend.communication.application.commands import CreateCommunicationCommand, UpdateCommunicationCommand, DeleteCommunicationCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.communication.handlers")

class CommunicationCommandHandler:
    def __init__(self, repository: ICommunicationRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateCommunicationCommand) -> CommunicationEntity:
        logger.info(f"Handling CreateCommunicationCommand: {cmd.code}")
        entity = CommunicationEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(CommunicationCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateCommunicationCommand) -> CommunicationEntity:
        logger.info(f"Handling UpdateCommunicationCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Communication", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(CommunicationUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteCommunicationCommand) -> bool:
        logger.info(f"Handling DeleteCommunicationCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for communication."""
    logger.info(f"Received domain event in communication: {event.event_type} (Aggregate: {event.aggregate_id})")
