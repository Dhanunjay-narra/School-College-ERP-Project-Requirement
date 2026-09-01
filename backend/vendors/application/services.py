"""
Vendor Management & Compliance — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.vendors.domain.entities import VendorsEntity
from backend.vendors.domain.repositories import IVendorsRepository
from backend.vendors.domain.events import VendorsCreatedEvent, VendorsUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class VendorsService:
    def __init__(self, repo: IVendorsRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> VendorsEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = VendorsEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(VendorsCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> VendorsEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Vendors", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[VendorsEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
