"""
Campus Infrastructure Projects — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.projects.domain.entities import ProjectsEntity

class IProjectsRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[ProjectsEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[ProjectsEntity]:
        pass

    @abstractmethod
    async def save(self, entity: ProjectsEntity) -> ProjectsEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
