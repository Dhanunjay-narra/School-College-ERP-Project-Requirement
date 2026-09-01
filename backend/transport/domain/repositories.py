"""
Transportation & GPS Fleet — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.transport.domain.entities import TransportEntity

class ITransportRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[TransportEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[TransportEntity]:
        pass

    @abstractmethod
    async def save(self, entity: TransportEntity) -> TransportEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
