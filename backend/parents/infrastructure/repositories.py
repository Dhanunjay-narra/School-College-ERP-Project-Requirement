"""
Parent & Guardian Management — Concrete Repository Implementation.
"""
from typing import List, Optional, Dict
import uuid
from backend.parents.domain.entities import ParentsEntity
from backend.parents.domain.repositories import IParentsRepository

class InMemoryParentsRepository(IParentsRepository):
    def __init__(self):
        self._items: Dict[str, ParentsEntity] = {}
        self._seed_sample_records()

    def _seed_sample_records(self):
        sample = ParentsEntity(
            id=f"PARENTS-001",
            code="SAMPLE-01",
            name="Primary Standard Parent & Guardian Management Record",
            status="ACTIVE",
            metadata={"description": "Parent profiles, authorized pickups, ward linkage, fee responsibility", "priority": "HIGH"}
        )
        self._items[sample.id] = sample

    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[ParentsEntity]:
        item = self._items.get(entity_id)
        if item and item.tenant_id == tenant_id:
            return item
        return None

    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[ParentsEntity]:
        tenant_items = [i for i in self._items.values() if i.tenant_id == tenant_id]
        return tenant_items[offset:offset+limit]

    async def save(self, entity: ParentsEntity) -> ParentsEntity:
        self._items[entity.id] = entity
        return entity

    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False

default_parents_repo = InMemoryParentsRepository()
