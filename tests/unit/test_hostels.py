"""
Unit Test Suite for Hostel & Housing Management (hostels).
"""
import pytest
import asyncio
from datetime import datetime
from backend.hostels.domain.entities import HostelsEntity
from backend.hostels.application.commands import CreateHostelsCommand, UpdateHostelsCommand, DeleteHostelsCommand
from backend.hostels.application.handlers import HostelsCommandHandler
from backend.hostels.infrastructure.repositories import InMemoryHostelsRepository
from backend.hostels.presentation.serializers import HostelsSerializer

def test_hostels_entity_creation():
    entity = HostelsEntity(code="TEST-01", name="Test Hostels Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_hostels_command_handler_flow():
    async def _run_flow():
        repo = InMemoryHostelsRepository()
        handler = HostelsCommandHandler(repo)

        create_cmd = CreateHostelsCommand(code="TEST-02", name="Automated Hostels")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateHostelsCommand(id=created.id, name="Updated Hostels")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Hostels"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteHostelsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_hostels_serializer():
    entity = HostelsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = HostelsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = HostelsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
