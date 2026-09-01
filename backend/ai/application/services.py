"""
AI/ML Predictive Intelligence — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.ai.domain.entities import AiEntity
from backend.ai.domain.repositories import IAiRepository
from backend.ai.domain.events import AiCreatedEvent, AiUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class AiService:
    def __init__(self, repo: IAiRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> AiEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = AiEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(AiCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> AiEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Ai", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[AiEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
