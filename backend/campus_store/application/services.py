"""
Campus Store & Cafeteria POS — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.campus_store.domain.entities import CampusStoreEntity
from backend.campus_store.domain.repositories import ICampusStoreRepository
from backend.campus_store.domain.events import CampusStoreCreatedEvent, CampusStoreUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class CampusStoreService:
    def __init__(self, repo: ICampusStoreRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> CampusStoreEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = CampusStoreEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(CampusStoreCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> CampusStoreEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Campus Store", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[CampusStoreEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
