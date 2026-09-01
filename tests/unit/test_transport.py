"""
Unit Test Suite for Transportation & GPS Fleet (transport).
"""
import pytest
import asyncio
from datetime import datetime
from backend.transport.domain.entities import TransportEntity
from backend.transport.application.commands import CreateTransportCommand, UpdateTransportCommand, DeleteTransportCommand
from backend.transport.application.handlers import TransportCommandHandler
from backend.transport.infrastructure.repositories import InMemoryTransportRepository
from backend.transport.presentation.serializers import TransportSerializer

def test_transport_entity_creation():
    entity = TransportEntity(code="TEST-01", name="Test Transport Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_transport_command_handler_flow():
    async def _run_flow():
        repo = InMemoryTransportRepository()
        handler = TransportCommandHandler(repo)

        create_cmd = CreateTransportCommand(code="TEST-02", name="Automated Transport")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateTransportCommand(id=created.id, name="Updated Transport")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Transport"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteTransportCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_transport_serializer():
    entity = TransportEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = TransportSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = TransportSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
