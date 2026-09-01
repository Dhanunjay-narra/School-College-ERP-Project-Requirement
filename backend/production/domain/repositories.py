"""
Campus Workshop & Fab Lab — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.production.domain.entities import ProductionEntity

class IProductionRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[ProductionEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[ProductionEntity]:
        pass

    @abstractmethod
    async def save(self, entity: ProductionEntity) -> ProductionEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
