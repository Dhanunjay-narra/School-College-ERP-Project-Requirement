"""
Configurable Workflow Engine — Concrete Repository Implementation.
"""
from typing import List, Optional, Dict
import uuid
from backend.workflows.domain.entities import WorkflowsEntity
from backend.workflows.domain.repositories import IWorkflowsRepository

class InMemoryWorkflowsRepository(IWorkflowsRepository):
    def __init__(self):
        self._items: Dict[str, WorkflowsEntity] = {}
        self._seed_sample_records()

    def _seed_sample_records(self):
        sample = WorkflowsEntity(
            id=f"WORKFLOWS-001",
            code="SAMPLE-01",
            name="Primary Standard Configurable Workflow Engine Record",
            status="ACTIVE",
            metadata={"description": "Multi-tier approval chains, dynamic triggers, SLA escalations, delegation", "priority": "HIGH"}
        )
        self._items[sample.id] = sample

    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[WorkflowsEntity]:
        item = self._items.get(entity_id)
        if item and item.tenant_id == tenant_id:
            return item
        return None

    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[WorkflowsEntity]:
        tenant_items = [i for i in self._items.values() if i.tenant_id == tenant_id]
        return tenant_items[offset:offset+limit]

    async def save(self, entity: WorkflowsEntity) -> WorkflowsEntity:
        self._items[entity.id] = entity
        return entity

    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False

default_workflows_repo = InMemoryWorkflowsRepository()
