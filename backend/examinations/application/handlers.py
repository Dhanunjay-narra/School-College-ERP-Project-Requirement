"""
Examinations & Grading — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for examinations.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.examinations.domain.entities import ExaminationsEntity
from backend.examinations.domain.repositories import IExaminationsRepository
from backend.examinations.domain.events import ExaminationsCreatedEvent, ExaminationsUpdatedEvent
from backend.examinations.application.commands import CreateExaminationsCommand, UpdateExaminationsCommand, DeleteExaminationsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.examinations.handlers")

class ExaminationsCommandHandler:
    def __init__(self, repository: IExaminationsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateExaminationsCommand) -> ExaminationsEntity:
        logger.info(f"Handling CreateExaminationsCommand: {cmd.code}")
        entity = ExaminationsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(ExaminationsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateExaminationsCommand) -> ExaminationsEntity:
        logger.info(f"Handling UpdateExaminationsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Examinations", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(ExaminationsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteExaminationsCommand) -> bool:
        logger.info(f"Handling DeleteExaminationsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for examinations."""
    logger.info(f"Received domain event in examinations: {event.event_type} (Aggregate: {event.aggregate_id})")
