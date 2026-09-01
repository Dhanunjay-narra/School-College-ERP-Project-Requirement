"""
Institutional CRM & Admissions Leads — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.crm.domain.entities import CrmEntity

class ICrmRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[CrmEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[CrmEntity]:
        pass

    @abstractmethod
    async def save(self, entity: CrmEntity) -> CrmEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
