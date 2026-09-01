"""
Repository Test Suite for Academic Structure & Timetable (academics).
"""
import pytest
import asyncio
from backend.academics.domain.entities import AcademicsEntity
from backend.academics.infrastructure.repositories import InMemoryAcademicsRepository

def test_academics_repository_crud():
    async def _run():
        repo = InMemoryAcademicsRepository()
        
        # Save entity
        entity = AcademicsEntity(code="R-TEST", name="Repository Test Academic Structure & Timetable", status="ACTIVE")
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
