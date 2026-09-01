"""
Document Management & Signatures — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.documents.domain.entities import DocumentsEntity

class IDocumentsRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[DocumentsEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[DocumentsEntity]:
        pass

    @abstractmethod
    async def save(self, entity: DocumentsEntity) -> DocumentsEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
