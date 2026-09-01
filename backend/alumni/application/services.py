"""
Alumni Network & Relations — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.alumni.domain.entities import AlumniEntity
from backend.alumni.domain.repositories import IAlumniRepository
from backend.alumni.domain.events import AlumniCreatedEvent, AlumniUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class AlumniService:
    def __init__(self, repo: IAlumniRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> AlumniEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = AlumniEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(AlumniCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> AlumniEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Alumni", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[AlumniEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
