"""
Repository Test Suite for Applicant Tracking System (recruitment).
"""
import pytest
import asyncio
from backend.recruitment.domain.entities import RecruitmentEntity
from backend.recruitment.infrastructure.repositories import InMemoryRecruitmentRepository

def test_recruitment_repository_crud():
    async def _run():
        repo = InMemoryRecruitmentRepository()
        
        # Save entity
        entity = RecruitmentEntity(code="R-TEST", name="Repository Test Applicant Tracking System", status="ACTIVE")
        saved = await repo.save(entity)
        assert saved.id is not None

        # Get entity
        fetched = await repo.get_by_id(saved.id)
        assert fetched is not None
        assert fetched.code == "R-TEST"

        # List entities
        items = await repo.list_all()
        assert len(items) >= 1

        # Delete entity
        deleted = await repo.delete(saved.id)
        assert deleted is True

    asyncio.run(_run())
