"""
Campus Store & Cafeteria POS — Concrete Repository Implementation.
"""
from typing import List, Optional, Dict
import uuid
from backend.campus_store.domain.entities import CampusStoreEntity
from backend.campus_store.domain.repositories import ICampusStoreRepository

class InMemoryCampusStoreRepository(ICampusStoreRepository):
    def __init__(self):
        self._items: Dict[str, CampusStoreEntity] = {}
        self._seed_sample_records()

    def _seed_sample_records(self):
        sample = CampusStoreEntity(
            id=f"CAMPUS_STORE-001",
            code="SAMPLE-01",
            name="Primary Standard Campus Store & Cafeteria POS Record",
            status="ACTIVE",
            metadata={"description": "POS billing, student digital wallet, bookstore, cafeteria menus", "priority": "HIGH"}
        )
        self._items[sample.id] = sample

    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[CampusStoreEntity]:
        item = self._items.get(entity_id)
        if item and item.tenant_id == tenant_id:
            return item
        return None

    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[CampusStoreEntity]:
        tenant_items = [i for i in self._items.values() if i.tenant_id == tenant_id]
        return tenant_items[offset:offset+limit]

    async def save(self, entity: CampusStoreEntity) -> CampusStoreEntity:
        self._items[entity.id] = entity
        return entity

    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False

default_campus_store_repo = InMemoryCampusStoreRepository()
