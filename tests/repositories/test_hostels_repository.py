"""
Repository Test Suite for Hostel & Housing Management (hostels).
"""
import pytest
import asyncio
from backend.hostels.domain.entities import HostelsEntity
from backend.hostels.infrastructure.repositories import InMemoryHostelsRepository

def test_hostels_repository_crud():
    async def _run():
        repo = InMemoryHostelsRepository()
        
        # Save entity
        entity = HostelsEntity(code="R-TEST", name="Repository Test Hostel & Housing Management", status="ACTIVE")
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
