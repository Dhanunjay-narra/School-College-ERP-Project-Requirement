"""
Finance & General Ledger — Concrete Repository Implementation.
"""
from typing import List, Optional, Dict
import uuid
from backend.finance.domain.entities import FinanceEntity
from backend.finance.domain.repositories import IFinanceRepository

class InMemoryFinanceRepository(IFinanceRepository):
    def __init__(self):
        self._items: Dict[str, FinanceEntity] = {}
        self._seed_sample_records()

    def _seed_sample_records(self):
        sample = FinanceEntity(
            id=f"FINANCE-001",
            code="SAMPLE-01",
            name="Primary Standard Finance & General Ledger Record",
            status="ACTIVE",
            metadata={"description": "Chart of Accounts, journal entries, trial balance, P&L, balance sheet, budgeting", "priority": "HIGH"}
        )
        self._items[sample.id] = sample

    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[FinanceEntity]:
        item = self._items.get(entity_id)
        if item and item.tenant_id == tenant_id:
            return item
        return None

    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[FinanceEntity]:
        tenant_items = [i for i in self._items.values() if i.tenant_id == tenant_id]
        return tenant_items[offset:offset+limit]

    async def save(self, entity: FinanceEntity) -> FinanceEntity:
        self._items[entity.id] = entity
        return entity

    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False

default_finance_repo = InMemoryFinanceRepository()
