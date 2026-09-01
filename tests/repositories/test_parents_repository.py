"""
Repository Test Suite for Parent & Guardian Management (parents).
"""
import pytest
import asyncio
from backend.parents.domain.entities import ParentsEntity
from backend.parents.infrastructure.repositories import InMemoryParentsRepository

def test_parents_repository_crud():
    async def _run():
        repo = InMemoryParentsRepository()
        
        # Save entity
        entity = ParentsEntity(code="R-TEST", name="Repository Test Parent & Guardian Management", status="ACTIVE")
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
