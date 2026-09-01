"""
Parent & Guardian Management — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.parents.domain.entities import ParentsEntity
from backend.parents.domain.repositories import IParentsRepository
from backend.parents.domain.events import ParentsCreatedEvent, ParentsUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class ParentsService:
    def __init__(self, repo: IParentsRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> ParentsEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = ParentsEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(ParentsCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> ParentsEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Parents", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[ParentsEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
