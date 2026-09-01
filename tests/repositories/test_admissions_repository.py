"""
Repository Test Suite for Admissions CRM & Merit Engine (admissions).
"""
import pytest
import asyncio
from backend.admissions.domain.entities import AdmissionsEntity
from backend.admissions.infrastructure.repositories import InMemoryAdmissionsRepository

def test_admissions_repository_crud():
    async def _run():
        repo = InMemoryAdmissionsRepository()
        
        # Save entity
        entity = AdmissionsEntity(code="R-TEST", name="Repository Test Admissions CRM & Merit Engine", status="ACTIVE")
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
