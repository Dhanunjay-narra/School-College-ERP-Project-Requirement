"""
Repository Test Suite for Research & Innovation Management (research).
"""
import pytest
import asyncio
from backend.research.domain.entities import ResearchEntity
from backend.research.infrastructure.repositories import InMemoryResearchRepository

def test_research_repository_crud():
    async def _run():
        repo = InMemoryResearchRepository()
        
        # Save entity
        entity = ResearchEntity(code="R-TEST", name="Repository Test Research & Innovation Management", status="ACTIVE")
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
