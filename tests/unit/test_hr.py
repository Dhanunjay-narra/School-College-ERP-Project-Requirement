"""
Unit Test Suite for Human Resource & Recruitment (hr).
"""
import pytest
import asyncio
from datetime import datetime
from backend.hr.domain.entities import HrEntity
from backend.hr.application.commands import CreateHrCommand, UpdateHrCommand, DeleteHrCommand
from backend.hr.application.handlers import HrCommandHandler
from backend.hr.infrastructure.repositories import InMemoryHrRepository
from backend.hr.presentation.serializers import HrSerializer

def test_hr_entity_creation():
    entity = HrEntity(code="TEST-01", name="Test Hr Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_hr_command_handler_flow():
    async def _run_flow():
        repo = InMemoryHrRepository()
        handler = HrCommandHandler(repo)

        create_cmd = CreateHrCommand(code="TEST-02", name="Automated Hr")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateHrCommand(id=created.id, name="Updated Hr")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Hr"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteHrCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_hr_serializer():
    entity = HrEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = HrSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = HrSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
