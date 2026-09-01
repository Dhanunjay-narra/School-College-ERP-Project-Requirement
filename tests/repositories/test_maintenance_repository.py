"""
Repository Test Suite for Campus Facility Maintenance (maintenance).
"""
import pytest
import asyncio
from backend.maintenance.domain.entities import MaintenanceEntity
from backend.maintenance.infrastructure.repositories import InMemoryMaintenanceRepository

def test_maintenance_repository_crud():
    async def _run():
        repo = InMemoryMaintenanceRepository()
        
        # Save entity
        entity = MaintenanceEntity(code="R-TEST", name="Repository Test Campus Facility Maintenance", status="ACTIVE")
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
