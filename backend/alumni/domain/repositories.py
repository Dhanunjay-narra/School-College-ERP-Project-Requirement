"""
Alumni Network & Relations — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.alumni.domain.entities import AlumniEntity

class IAlumniRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[AlumniEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[AlumniEntity]:
        pass

    @abstractmethod
    async def save(self, entity: AlumniEntity) -> AlumniEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
