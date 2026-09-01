"""
Repository Test Suite for Institutional CRM & Admissions Leads (crm).
"""
import pytest
import asyncio
from backend.crm.domain.entities import CrmEntity
from backend.crm.infrastructure.repositories import InMemoryCrmRepository

def test_crm_repository_crud():
    async def _run():
        repo = InMemoryCrmRepository()
        
        # Save entity
        entity = CrmEntity(code="R-TEST", name="Repository Test Institutional CRM & Admissions Leads", status="ACTIVE")
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
