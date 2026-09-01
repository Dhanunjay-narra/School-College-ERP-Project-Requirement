"""
Repository Test Suite for Campus Store & Cafeteria POS (campus_store).
"""
import pytest
import asyncio
from backend.campus_store.domain.entities import CampusStoreEntity
from backend.campus_store.infrastructure.repositories import InMemoryCampusStoreRepository

def test_campus_store_repository_crud():
    async def _run():
        repo = InMemoryCampusStoreRepository()
        
        # Save entity
        entity = CampusStoreEntity(code="R-TEST", name="Repository Test Campus Store & Cafeteria POS", status="ACTIVE")
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
