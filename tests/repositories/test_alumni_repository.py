"""
Repository Test Suite for Alumni Network & Relations (alumni).
"""
import pytest
import asyncio
from backend.alumni.domain.entities import AlumniEntity
from backend.alumni.infrastructure.repositories import InMemoryAlumniRepository

def test_alumni_repository_crud():
    async def _run():
        repo = InMemoryAlumniRepository()
        
        # Save entity
        entity = AlumniEntity(code="R-TEST", name="Repository Test Alumni Network & Relations", status="ACTIVE")
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
