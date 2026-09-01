"""
Repository Test Suite for Campus Events & Conferences (events).
"""
import pytest
import asyncio
from backend.events.domain.entities import EventsEntity
from backend.events.infrastructure.repositories import InMemoryEventsRepository

def test_events_repository_crud():
    async def _run():
        repo = InMemoryEventsRepository()
        
        # Save entity
        entity = EventsEntity(code="R-TEST", name="Repository Test Campus Events & Conferences", status="ACTIVE")
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
