"""
Repository Test Suite for Library & RFID Circulation (library).
"""
import pytest
import asyncio
from backend.library.domain.entities import LibraryEntity
from backend.library.infrastructure.repositories import InMemoryLibraryRepository

def test_library_repository_crud():
    async def _run():
        repo = InMemoryLibraryRepository()
        
        # Save entity
        entity = LibraryEntity(code="R-TEST", name="Repository Test Library & RFID Circulation", status="ACTIVE")
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
