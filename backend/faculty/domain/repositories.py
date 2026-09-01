"""
Faculty & Workload Management — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.faculty.domain.entities import FacultyEntity

class IFacultyRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[FacultyEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[FacultyEntity]:
        pass

    @abstractmethod
    async def save(self, entity: FacultyEntity) -> FacultyEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
