"""
Campus Infrastructure Projects — Application Use Cases & Domain Services.
"""
from typing import List, Optional, Dict, Any
from backend.projects.domain.entities import ProjectsEntity
from backend.projects.domain.repositories import IProjectsRepository
from backend.projects.domain.events import ProjectsCreatedEvent, ProjectsUpdatedEvent
from backend.core.events import event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

class ProjectsService:
    def __init__(self, repo: IProjectsRepository):
        self.repo = repo

    async def create_item(self, code: str, name: str, status: str = "ACTIVE", tenant_id: str = "default_institution", metadata: Optional[Dict[str, Any]] = None) -> ProjectsEntity:
        if not code or not name:
            raise ValidationException("Code and Name are required fields.")
        
        entity = ProjectsEntity(
            code=code,
            name=name,
            status=status,
            tenant_id=tenant_id,
            metadata=metadata
        )
        saved = await self.repo.save(entity)
        await event_bus.publish(ProjectsCreatedEvent(saved.id, tenant_id, saved.to_dict()))
        return saved

    async def get_item(self, item_id: str, tenant_id: str = "default_institution") -> ProjectsEntity:
        item = await self.repo.get_by_id(item_id, tenant_id)
        if not item:
            raise EntityNotFoundException("Projects", item_id)
        return item

    async def list_items(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[ProjectsEntity]:
        return await self.repo.list_all(tenant_id, limit, offset)
