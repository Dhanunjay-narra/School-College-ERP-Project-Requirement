"""
Centralized Faceted Search — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.search.domain.entities import SearchEntity
from backend.search.domain.repositories import ISearchRepository
from backend.search.domain.events import SearchCreatedEvent, SearchUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class SearchService:
    def __init__(self, repo: ISearchRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> SearchEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = SearchEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(SearchCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> SearchEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Search", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[SearchEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
