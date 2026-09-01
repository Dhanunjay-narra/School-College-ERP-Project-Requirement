"""
Configurable Workflow Engine — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for workflows.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.workflows.domain.entities import WorkflowsEntity
from backend.workflows.domain.repositories import IWorkflowsRepository
from backend.workflows.domain.events import WorkflowsCreatedEvent, WorkflowsUpdatedEvent
from backend.workflows.application.commands import CreateWorkflowsCommand, UpdateWorkflowsCommand, DeleteWorkflowsCommand
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.workflows.handlers")

class WorkflowsCommandHandler:
    def __init__(self, repository: IWorkflowsRepository):
        self.repository = repository

    async def handle_create(self, cmd: CreateWorkflowsCommand) -> WorkflowsEntity:
        logger.info(f"Handling CreateWorkflowsCommand: {cmd.code}")
        entity = WorkflowsEntity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish(WorkflowsCreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: UpdateWorkflowsCommand) -> WorkflowsEntity:
        logger.info(f"Handling UpdateWorkflowsCommand for ID: {cmd.id}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("Workflows", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish(WorkflowsUpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: DeleteWorkflowsCommand) -> bool:
        logger.info(f"Handling DeleteWorkflowsCommand for ID: {cmd.id} (Reason: {cmd.reason})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for workflows."""
    logger.info(f"Received domain event in workflows: {event.event_type} (Aggregate: {event.aggregate_id})")
