"""
Campus Workshop & Fab Lab — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.production.domain.entities import ProductionEntity
from backend.production.domain.repositories import IProductionRepository
from backend.production.domain.events import ProductionCreatedEvent, ProductionUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class ProductionService:
    def __init__(self, repo: IProductionRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> ProductionEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = ProductionEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(ProductionCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> ProductionEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Production", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[ProductionEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
