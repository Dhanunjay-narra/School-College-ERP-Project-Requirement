"""
Campus Infrastructure Projects — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for projects.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.projects.domain.entities import ProjectsEntity
from backend.projects.domain.repositories import IProjectsRepository
from backend.projects.domain.events import ProjectsCreatedEvent, ProjectsUpdatedEvent
from backend.projects.application.commands import CreateProjectsCommand, UpdateProjectsCommand, DeleteProjectsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.projects.handlers")

class ProjectsCommandHandler:
    def __init__(self, repository: IProjectsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateProjectsCommand) -> ProjectsEntity:
        logger.info(f"Handling CreateProjectsCommand: {cmd.code}")
        entity = ProjectsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(ProjectsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateProjectsCommand) -> ProjectsEntity:
        logger.info(f"Handling UpdateProjectsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Projects", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(ProjectsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteProjectsCommand) -> bool:
        logger.info(f"Handling DeleteProjectsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for projects."""
    logger.info(f"Received domain event in projects: {event.event_type} (Aggregate: {event.aggregate_id})")
