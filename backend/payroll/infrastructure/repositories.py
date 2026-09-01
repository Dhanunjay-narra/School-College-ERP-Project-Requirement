"""
Integrated Payroll Engine — Concrete Repository Implementation.
"""
from typing import List, Optional, Dict
import uuid
from backend.payroll.domain.entities import PayrollEntity
from backend.payroll.domain.repositories import IPayrollRepository

class InMemoryPayrollRepository(IPayrollRepository):
    def __init__(self):
        self._items: Dict[str, PayrollEntity] = {}
        self._seed_sample_records()

    def _seed_sample_records(self):
        sample = PayrollEntity(
            id=f"PAYROLL-001",
            code="SAMPLE-01",
            name="Primary Standard Integrated Payroll Engine Record",
            status="ACTIVE",
            metadata={"description": "Salary structures, basic, allowances, deductions, PF, TDS, direct bank transfers", "priority": "HIGH"}
        )
        self._items[sample.id] = sample

    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[PayrollEntity]:
        item = self._items.get(entity_id)
        if item and item.tenant_id == tenant_id:
            return item
        return None

    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[PayrollEntity]:
        tenant_items = [i for i in self._items.values() if i.tenant_id == tenant_id]
        return tenant_items[offset:offset+limit]

    async def save(self, entity: PayrollEntity) -> PayrollEntity:
        self._items[entity.id] = entity
        return entity

    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False

default_payroll_repo = InMemoryPayrollRepository()
