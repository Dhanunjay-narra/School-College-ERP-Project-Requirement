"""
Unit Test Suite for Universal Multi-Channel Notifications (communication).
"""
import pytest
import asyncio
from datetime import datetime
from backend.communication.domain.entities import CommunicationEntity
from backend.communication.application.commands import CreateCommunicationCommand, UpdateCommunicationCommand, DeleteCommunicationCommand
from backend.communication.application.handlers import CommunicationCommandHandler
from backend.communication.infrastructure.repositories import InMemoryCommunicationRepository
from backend.communication.presentation.serializers import CommunicationSerializer

def test_communication_entity_creation():
    entity = CommunicationEntity(code="TEST-01", name="Test Communication Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_communication_command_handler_flow():
    async def _run_flow():
        repo = InMemoryCommunicationRepository()
        handler = CommunicationCommandHandler(repo)

        create_cmd = CreateCommunicationCommand(code="TEST-02", name="Automated Communication")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateCommunicationCommand(id=created.id, name="Updated Communication")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Communication"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteCommunicationCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_communication_serializer():
    entity = CommunicationEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = CommunicationSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = CommunicationSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
