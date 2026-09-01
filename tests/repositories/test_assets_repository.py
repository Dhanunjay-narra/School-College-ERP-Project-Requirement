"""
Repository Test Suite for Asset Lifecycle & Depreciation (assets).
"""
import pytest
import asyncio
from backend.assets.domain.entities import AssetsEntity
from backend.assets.infrastructure.repositories import InMemoryAssetsRepository

def test_assets_repository_crud():
    async def _run():
        repo = InMemoryAssetsRepository()
        
        # Save entity
        entity = AssetsEntity(code="R-TEST", name="Repository Test Asset Lifecycle & Depreciation", status="ACTIVE")
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
