"""
Accreditation & Regulatory Compliance — Concrete Repository Implementation.
"""
from typing import List, Optional, Dict
import uuid
from backend.compliance.domain.entities import ComplianceEntity
from backend.compliance.domain.repositories import IComplianceRepository

class InMemoryComplianceRepository(IComplianceRepository):
    def __init__(self):
        self._items: Dict[str, ComplianceEntity] = {}
        self._seed_sample_records()

    def _seed_sample_records(self):
        sample = ComplianceEntity(
            id=f"COMPLIANCE-001",
            code="SAMPLE-01",
            name="Primary Standard Accreditation & Regulatory Compliance Record",
            status="ACTIVE",
            metadata={"description": "NAAC, NBA, ABET, ISO compliance documentation, audit trails", "priority": "HIGH"}
        )
        self._items[sample.id] = sample

    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[ComplianceEntity]:
        item = self._items.get(entity_id)
        if item and item.tenant_id == tenant_id:
            return item
        return None

    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[ComplianceEntity]:
        tenant_items = [i for i in self._items.values() if i.tenant_id == tenant_id]
        return tenant_items[offset:offset+limit]

    async def save(self, entity: ComplianceEntity) -> ComplianceEntity:
        self._items[entity.id] = entity
        return entity

    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False

default_compliance_repo = InMemoryComplianceRepository()
