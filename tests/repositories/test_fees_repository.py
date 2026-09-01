"""
Repository Test Suite for Fees & Student Billing (fees).
"""
import pytest
import asyncio
from backend.fees.domain.entities import FeesEntity
from backend.fees.infrastructure.repositories import InMemoryFeesRepository

def test_fees_repository_crud():
    async def _run():
        repo = InMemoryFeesRepository()
        
        # Save entity
        entity = FeesEntity(code="R-TEST", name="Repository Test Fees & Student Billing", status="ACTIVE")
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
