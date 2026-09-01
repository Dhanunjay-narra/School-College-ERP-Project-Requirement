"""
Repository Test Suite for Vendor Management & Compliance (vendors).
"""
import pytest
import asyncio
from backend.vendors.domain.entities import VendorsEntity
from backend.vendors.infrastructure.repositories import InMemoryVendorsRepository

def test_vendors_repository_crud():
    async def _run():
        repo = InMemoryVendorsRepository()
        
        # Save entity
        entity = VendorsEntity(code="R-TEST", name="Repository Test Vendor Management & Compliance", status="ACTIVE")
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
