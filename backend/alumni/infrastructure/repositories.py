"""
Alumni Network & Relations — Concrete Repository Implementation.
"""
from typing import List, Optional, Dict
import uuid
from backend.alumni.domain.entities import AlumniEntity
from backend.alumni.domain.repositories import IAlumniRepository

class InMemoryAlumniRepository(IAlumniRepository):
    def __init__(self):
        self._items: Dict[str, AlumniEntity] = {}
        self._seed_sample_records()

    def _seed_sample_records(self):
        sample = AlumniEntity(
            id=f"ALUMNI-001",
            code="SAMPLE-01",
            name="Primary Standard Alumni Network & Relations Record",
            status="ACTIVE",
            metadata={"description": "Alumni directory, reunions, donations, mentorship pairings, career network", "priority": "HIGH"}
        )
        self._items[sample.id] = sample

    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[AlumniEntity]:
        item = self._items.get(entity_id)
        if item and item.tenant_id == tenant_id:
            return item
        return None

    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[AlumniEntity]:
        tenant_items = [i for i in self._items.values() if i.tenant_id == tenant_id]
        return tenant_items[offset:offset+limit]

    async def save(self, entity: AlumniEntity) -> AlumniEntity:
        self._items[entity.id] = entity
        return entity

    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False

default_alumni_repo = InMemoryAlumniRepository()
