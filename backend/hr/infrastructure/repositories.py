"""
Human Resource & Recruitment — Concrete Repository Implementation.
"""
from typing import List, Optional, Dict
import uuid
from backend.hr.domain.entities import HrEntity
from backend.hr.domain.repositories import IHrRepository

class InMemoryHrRepository(IHrRepository):
    def __init__(self):
        self._items: Dict[str, HrEntity] = {}
        self._seed_sample_records()

    def _seed_sample_records(self):
        sample = HrEntity(
            id=f"HR-001",
            code="SAMPLE-01",
            name="Primary Standard Human Resource & Recruitment Record",
            status="ACTIVE",
            metadata={"description": "Employee records, contracts, recruitment ATS, leave policies, promotions", "priority": "HIGH"}
        )
        self._items[sample.id] = sample

    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[HrEntity]:
        item = self._items.get(entity_id)
        if item and item.tenant_id == tenant_id:
            return item
        return None

    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[HrEntity]:
        tenant_items = [i for i in self._items.values() if i.tenant_id == tenant_id]
        return tenant_items[offset:offset+limit]

    async def save(self, entity: HrEntity) -> HrEntity:
        self._items[entity.id] = entity
        return entity

    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False

default_hr_repo = InMemoryHrRepository()
