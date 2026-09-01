"""
Academic Structure & Timetable — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.academics.domain.entities import AcademicsEntity
from backend.academics.domain.repositories import IAcademicsRepository
from backend.academics.domain.events import AcademicsCreatedEvent, AcademicsUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class AcademicsService:
    def __init__(self, repo: IAcademicsRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> AcademicsEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = AcademicsEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(AcademicsCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> AcademicsEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Academics", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[AcademicsEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
