"""
Configurable Workflow Engine — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.workflows.domain.entities import WorkflowsEntity
from backend.workflows.domain.repositories import IWorkflowsRepository
from backend.workflows.domain.events import WorkflowsCreatedEvent, WorkflowsUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class WorkflowsService:
    def __init__(self, repo: IWorkflowsRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> WorkflowsEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = WorkflowsEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(WorkflowsCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> WorkflowsEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Workflows", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[WorkflowsEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
