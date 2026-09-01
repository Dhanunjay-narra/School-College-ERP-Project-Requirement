"""
Unit Test Suite for Fees & Student Billing (fees).
"""
import pytest
import asyncio
from datetime import datetime
from backend.fees.domain.entities import FeesEntity
from backend.fees.application.commands import CreateFeesCommand, UpdateFeesCommand, DeleteFeesCommand
from backend.fees.application.handlers import FeesCommandHandler
from backend.fees.infrastructure.repositories import InMemoryFeesRepository
from backend.fees.presentation.serializers import FeesSerializer

def test_fees_entity_creation():
    entity = FeesEntity(code="TEST-01", name="Test Fees Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_fees_command_handler_flow():
    async def _run_flow():
        repo = InMemoryFeesRepository()
        handler = FeesCommandHandler(repo)

        create_cmd = CreateFeesCommand(code="TEST-02", name="Automated Fees")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateFeesCommand(id=created.id, name="Updated Fees")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Fees"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteFeesCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_fees_serializer():
    entity = FeesEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = FeesSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = FeesSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
