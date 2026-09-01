"""
Unit Test Suite for Multi-Store Warehouse Management (warehouses).
"""
import pytest
import asyncio
from datetime import datetime
from backend.warehouses.domain.entities import WarehousesEntity
from backend.warehouses.application.commands import CreateWarehousesCommand, UpdateWarehousesCommand, DeleteWarehousesCommand
from backend.warehouses.application.handlers import WarehousesCommandHandler
from backend.warehouses.infrastructure.repositories import InMemoryWarehousesRepository
from backend.warehouses.presentation.serializers import WarehousesSerializer

def test_warehouses_entity_creation():
    entity = WarehousesEntity(code="TEST-01", name="Test Warehouses Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_warehouses_command_handler_flow():
    async def _run_flow():
        repo = InMemoryWarehousesRepository()
        handler = WarehousesCommandHandler(repo)

        create_cmd = CreateWarehousesCommand(code="TEST-02", name="Automated Warehouses")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateWarehousesCommand(id=created.id, name="Updated Warehouses")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Warehouses"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteWarehousesCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_warehouses_serializer():
    entity = WarehousesEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = WarehousesSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = WarehousesSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
