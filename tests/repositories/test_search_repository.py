"""
Repository Test Suite for Centralized Faceted Search (search).
"""
import pytest
import asyncio
from backend.search.domain.entities import SearchEntity
from backend.search.infrastructure.repositories import InMemorySearchRepository

def test_search_repository_crud():
    async def _run():
        repo = InMemorySearchRepository()
        
        # Save entity
        entity = SearchEntity(code="R-TEST", name="Repository Test Centralized Faceted Search", status="ACTIVE")
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
