"""
Parent & Guardian Management — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.parents.domain.entities import ParentsEntity

class IParentsRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[ParentsEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[ParentsEntity]:
        pass

    @abstractmethod
    async def save(self, entity: ParentsEntity) -> ParentsEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
