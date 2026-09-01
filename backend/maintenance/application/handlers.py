"""
Campus Facility Maintenance — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for maintenance.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.maintenance.domain.entities import MaintenanceEntity
from backend.maintenance.domain.repositories import IMaintenanceRepository
from backend.maintenance.domain.events import MaintenanceCreatedEvent, MaintenanceUpdatedEvent
from backend.maintenance.application.commands import CreateMaintenanceCommand, UpdateMaintenanceCommand, DeleteMaintenanceCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.maintenance.handlers")

class MaintenanceCommandHandler:
    def __init__(self, repository: IMaintenanceRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateMaintenanceCommand) -> MaintenanceEntity:
        logger.info(f"Handling CreateMaintenanceCommand: {cmd.code}")
        entity = MaintenanceEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(MaintenanceCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateMaintenanceCommand) -> MaintenanceEntity:
        logger.info(f"Handling UpdateMaintenanceCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Maintenance", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(MaintenanceUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteMaintenanceCommand) -> bool:
        logger.info(f"Handling DeleteMaintenanceCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for maintenance."""
    logger.info(f"Received domain event in maintenance: {event.event_type} (Aggregate: {event.aggregate_id})")
