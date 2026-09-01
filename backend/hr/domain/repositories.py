"""
Human Resource & Recruitment — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.hr.domain.entities import HrEntity

class IHrRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[HrEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[HrEntity]:
        pass

    @abstractmethod
    async def save(self, entity: HrEntity) -> HrEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
