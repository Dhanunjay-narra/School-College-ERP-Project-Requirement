"""
Applicant Tracking System — Concrete Repository Implementation.
"""
from typing import List, Optional, Dict
import uuid
from backend.recruitment.domain.entities import RecruitmentEntity
from backend.recruitment.domain.repositories import IRecruitmentRepository

class InMemoryRecruitmentRepository(IRecruitmentRepository):
    def __init__(self):
        self._items: Dict[str, RecruitmentEntity] = {}
        self._seed_sample_records()

    def _seed_sample_records(self):
        sample = RecruitmentEntity(
            id=f"RECRUITMENT-001",
            code="SAMPLE-01",
            name="Primary Standard Applicant Tracking System Record",
            status="ACTIVE",
            metadata={"description": "Job postings, applicant screening, interview rounds, offer letters", "priority": "HIGH"}
        )
        self._items[sample.id] = sample

    async def get_by_id(self, entity_id: str, tenant_id: str = "default_institution") -> Optional[RecruitmentEntity]:
        item = self._items.get(entity_id)
        if item and item.tenant_id == tenant_id:
            return item
        return None

    async def list_all(self, tenant_id: str = "default_institution", limit: int = 50, offset: int = 0) -> List[RecruitmentEntity]:
        tenant_items = [i for i in self._items.values() if i.tenant_id == tenant_id]
        return tenant_items[offset:offset+limit]

    async def save(self, entity: RecruitmentEntity) -> RecruitmentEntity:
        self._items[entity.id] = entity
        return entity

    async def delete(self, entity_id: str, tenant_id: str = "default_institution") -> bool:
        if entity_id in self._items:
            del self._items[entity_id]
            return True
        return False

default_recruitment_repo = InMemoryRecruitmentRepository()
