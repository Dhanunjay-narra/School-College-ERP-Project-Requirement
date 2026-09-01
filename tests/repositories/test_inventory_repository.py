"""
Repository Test Suite for Campus Inventory & Stores (inventory).
"""
import pytest
import asyncio
from backend.inventory.domain.entities import InventoryEntity
from backend.inventory.infrastructure.repositories import InMemoryInventoryRepository

def test_inventory_repository_crud():
    async def _run():
        repo = InMemoryInventoryRepository()
        
        # Save entity
        entity = InventoryEntity(code="R-TEST", name="Repository Test Campus Inventory & Stores", status="ACTIVE")
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
