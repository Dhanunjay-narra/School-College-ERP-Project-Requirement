"""
Hostel & Housing Management — Concrete Repository Implementation.
"""
from typing import List, Optional, Dict
import uuid
from backend.hostels.domain.entities import HostelsEntity
from backend.hostels.domain.repositories import IHostelsRepository

class InMemoryHostelsRepository(IHostelsRepository):
    def __init__(self):
        self._items: Dict[str, HostelsEntity] = {}
        self._seed_sample_records()

    def _seed_sample_records(self):
        sample = HostelsEntity(
            id=f"HOSTELS-001",
            code="SAMPLE-01",
            name="Primary Standard Hostel & Housing Management Record",
            status="ACTIVE",
            metadata={"description": "Buildings, rooms, bed allocations, mess menus, outpass approvals, visitors", "priority": "HIGH"}
        )
        self._items[sample.id] = sample

    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[HostelsEntity]:
        item = self._items.get(entity_id)
        if item and item.tenant_id == tenant_id:
            return item
        return None

    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[HostelsEntity]:
        tenant_items = [i for i in self._items.values() if i.tenant_id == tenant_id]
        return tenant_items[offset:offset+limit]

    async def save(self, entity: HostelsEntity) -> HostelsEntity:
        self._items[entity.id] = entity
        return entity

    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False

default_hostels_repo = InMemoryHostelsRepository()
