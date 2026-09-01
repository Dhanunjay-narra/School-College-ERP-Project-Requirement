"""
Unit Test Suite for Campus Inventory & Stores (inventory).
"""
import pytest
import asyncio
from datetime import datetime
from backend.inventory.domain.entities import InventoryEntity
from backend.inventory.application.commands import CreateInventoryCommand, UpdateInventoryCommand, DeleteInventoryCommand
from backend.inventory.application.handlers import InventoryCommandHandler
from backend.inventory.infrastructure.repositories import InMemoryInventoryRepository
from backend.inventory.presentation.serializers import InventorySerializer

def test_inventory_entity_creation():
    entity = InventoryEntity(code="TEST-01", name="Test Inventory Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_inventory_command_handler_flow():
    async def _run_flow():
        repo = InMemoryInventoryRepository()
        handler = InventoryCommandHandler(repo)

        create_cmd = CreateInventoryCommand(code="TEST-02", name="Automated Inventory")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateInventoryCommand(id=created.id, name="Updated Inventory")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Inventory"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteInventoryCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_inventory_serializer():
    entity = InventoryEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = InventorySerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = InventorySerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
