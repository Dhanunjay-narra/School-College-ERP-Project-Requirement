"""
Unit Test Suite for Vendor Management & Compliance (vendors).
"""
import pytest
import asyncio
from datetime import datetime
from backend.vendors.domain.entities import VendorsEntity
from backend.vendors.application.commands import CreateVendorsCommand, UpdateVendorsCommand, DeleteVendorsCommand
from backend.vendors.application.handlers import VendorsCommandHandler
from backend.vendors.infrastructure.repositories import InMemoryVendorsRepository
from backend.vendors.presentation.serializers import VendorsSerializer

def test_vendors_entity_creation():
    entity = VendorsEntity(code="TEST-01", name="Test Vendors Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_vendors_command_handler_flow():
    async def _run_flow():
        repo = InMemoryVendorsRepository()
        handler = VendorsCommandHandler(repo)

        create_cmd = CreateVendorsCommand(code="TEST-02", name="Automated Vendors")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateVendorsCommand(id=created.id, name="Updated Vendors")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Vendors"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteVendorsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_vendors_serializer():
    entity = VendorsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = VendorsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = VendorsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
