"""
Multi-Store Warehouse Management — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.warehouses.domain.entities import WarehousesEntity

class IWarehousesRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[WarehousesEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[WarehousesEntity]:
        pass

    @abstractmethod
    async def save(self, entity: WarehousesEntity) -> WarehousesEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
