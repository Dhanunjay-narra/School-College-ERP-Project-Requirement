"""
Campus Store & Cafeteria POS — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.campus_store.domain.entities import CampusStoreEntity

class ICampusStoreRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[CampusStoreEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[CampusStoreEntity]:
        pass

    @abstractmethod
    async def save(self, entity: CampusStoreEntity) -> CampusStoreEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
