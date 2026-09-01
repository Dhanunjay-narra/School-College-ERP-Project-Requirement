"""
Campus Inventory & Stores — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.inventory.domain.entities import InventoryEntity
from backend.inventory.domain.repositories import IInventoryRepository
from backend.inventory.domain.events import InventoryCreatedEvent, InventoryUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class InventoryService:
    def __init__(self, repo: IInventoryRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> InventoryEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = InventoryEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(InventoryCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> InventoryEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Inventory", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[InventoryEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
