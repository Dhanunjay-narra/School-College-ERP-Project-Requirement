"""
Transportation & GPS Fleet — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for transport.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.transport.domain.entities import TransportEntity
from backend.transport.domain.repositories import ITransportRepository
from backend.transport.domain.events import TransportCreatedEvent, TransportUpdatedEvent
from backend.transport.application.commands import CreateTransportCommand, UpdateTransportCommand, DeleteTransportCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.transport.handlers")

class TransportCommandHandler:
    def __init__(self, repository: ITransportRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateTransportCommand) -> TransportEntity:
        logger.info(f"Handling CreateTransportCommand: {cmd.code}")
        entity = TransportEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(TransportCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateTransportCommand) -> TransportEntity:
        logger.info(f"Handling UpdateTransportCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Transport", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(TransportUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteTransportCommand) -> bool:
        logger.info(f"Handling DeleteTransportCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for transport."""
    logger.info(f"Received domain event in transport: {event.event_type} (Aggregate: {event.aggregate_id})")
