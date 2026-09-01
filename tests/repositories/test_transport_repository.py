"""
Repository Test Suite for Transportation & GPS Fleet (transport).
"""
import pytest
import asyncio
from backend.transport.domain.entities import TransportEntity
from backend.transport.infrastructure.repositories import InMemoryTransportRepository

def test_transport_repository_crud():
    async def _run():
        repo = InMemoryTransportRepository()
        
        # Save entity
        entity = TransportEntity(code="R-TEST", name="Repository Test Transportation & GPS Fleet", status="ACTIVE")
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
