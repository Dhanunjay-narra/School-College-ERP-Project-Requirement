"""
Campus Facility Maintenance — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.maintenance.domain.entities import MaintenanceEntity

class IMaintenanceRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[MaintenanceEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[MaintenanceEntity]:
        pass

    @abstractmethod
    async def save(self, entity: MaintenanceEntity) -> MaintenanceEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
