"""
Repository Test Suite for Campus Workshop & Fab Lab (production).
"""
import pytest
import asyncio
from backend.production.domain.entities import ProductionEntity
from backend.production.infrastructure.repositories import InMemoryProductionRepository

def test_production_repository_crud():
    async def _run():
        repo = InMemoryProductionRepository()
        
        # Save entity
        entity = ProductionEntity(code="R-TEST", name="Repository Test Campus Workshop & Fab Lab", status="ACTIVE")
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
