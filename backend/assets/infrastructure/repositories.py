"""
Asset Lifecycle & Depreciation — Concrete Repository Implementation.
"""
from typing import List, Optional, Dict
import uuid
from backend.assets.domain.entities import AssetsEntity
from backend.assets.domain.repositories import IAssetsRepository

class InMemoryAssetsRepository(IAssetsRepository):
    def __init__(self):
        self._items: Dict[str, AssetsEntity] = {}
        self._seed_sample_records()

    def _seed_sample_records(self):
        sample = AssetsEntity(
            id=f"ASSETS-001",
            code="SAMPLE-01",
            name="Primary Standard Asset Lifecycle & Depreciation Record",
            status="ACTIVE",
            metadata={"description": "Asset tagging, QR/barcodes, straight-line depreciation, maintenance", "priority": "HIGH"}
        )
        self._items[sample.id] = sample

    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[AssetsEntity]:
        item = self._items.get(entity_id)
        if item and item.tenant_id == tenant_id:
            return item
        return None

    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[AssetsEntity]:
        tenant_items = [i for i in self._items.values() if i.tenant_id == tenant_id]
        return tenant_items[offset:offset+limit]

    async def save(self, entity: AssetsEntity) -> AssetsEntity:
        self._items[entity.id] = entity
        return entity

    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False

default_assets_repo = InMemoryAssetsRepository()
