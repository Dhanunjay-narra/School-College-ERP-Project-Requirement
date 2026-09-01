"""
Admissions CRM & Merit Engine — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for admissions.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.admissions.domain.entities import AdmissionsEntity
from backend.admissions.domain.repositories import IAdmissionsRepository
from backend.admissions.domain.events import AdmissionsCreatedEvent, AdmissionsUpdatedEvent
from backend.admissions.application.commands import CreateAdmissionsCommand, UpdateAdmissionsCommand, DeleteAdmissionsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.admissions.handlers")

class AdmissionsCommandHandler:
    def __init__(self, repository: IAdmissionsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateAdmissionsCommand) -> AdmissionsEntity:
        logger.info(f"Handling CreateAdmissionsCommand: {cmd.code}")
        entity = AdmissionsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(AdmissionsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateAdmissionsCommand) -> AdmissionsEntity:
        logger.info(f"Handling UpdateAdmissionsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Admissions", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(AdmissionsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteAdmissionsCommand) -> bool:
        logger.info(f"Handling DeleteAdmissionsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for admissions."""
    logger.info(f"Received domain event in admissions: {event.event_type} (Aggregate: {event.aggregate_id})")
