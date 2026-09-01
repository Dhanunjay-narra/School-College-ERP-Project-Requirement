"""
Admissions CRM & Merit Engine — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.admissions.domain.entities import AdmissionsEntity

class IAdmissionsRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[AdmissionsEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[AdmissionsEntity]:
        pass

    @abstractmethod
    async def save(self, entity: AdmissionsEntity) -> AdmissionsEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
