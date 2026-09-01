"""
Applicant Tracking System — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for recruitment.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.recruitment.domain.entities import RecruitmentEntity
from backend.recruitment.domain.repositories import IRecruitmentRepository
from backend.recruitment.domain.events import RecruitmentCreatedEvent, RecruitmentUpdatedEvent
from backend.recruitment.application.commands import CreateRecruitmentCommand, UpdateRecruitmentCommand, DeleteRecruitmentCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.recruitment.handlers")

class RecruitmentCommandHandler:
    def __init__(self, repository: IRecruitmentRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateRecruitmentCommand) -> RecruitmentEntity:
        logger.info(f"Handling CreateRecruitmentCommand: {cmd.code}")
        entity = RecruitmentEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(RecruitmentCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateRecruitmentCommand) -> RecruitmentEntity:
        logger.info(f"Handling UpdateRecruitmentCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Recruitment", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(RecruitmentUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteRecruitmentCommand) -> bool:
        logger.info(f"Handling DeleteRecruitmentCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for recruitment."""
    logger.info(f"Received domain event in recruitment: {event.event_type} (Aggregate: {event.aggregate_id})")
