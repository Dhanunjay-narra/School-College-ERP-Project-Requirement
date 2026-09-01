"""
Integrated Payroll Engine — Repository Interface.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from backend.payroll.domain.entities import PayrollEntity

class IPayrollRepository(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[PayrollEntity]:
        pass

    @abstractmethod
    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[PayrollEntity]:
        pass

    @abstractmethod
    async def save(self, entity: PayrollEntity) -> PayrollEntity:
        pass

    @abstractmethod
    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        pass
