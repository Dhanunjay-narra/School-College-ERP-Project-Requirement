"""
Unit Test Suite for Academic Structure & Timetable (academics).
"""
import pytest
import asyncio
from datetime import datetime
from backend.academics.domain.entities import AcademicsEntity
from backend.academics.application.commands import CreateAcademicsCommand, UpdateAcademicsCommand, DeleteAcademicsCommand
from backend.academics.application.handlers import AcademicsCommandHandler
from backend.academics.infrastructure.repositories import InMemoryAcademicsRepository
from backend.academics.presentation.serializers import AcademicsSerializer

def test_academics_entity_creation():
    entity = AcademicsEntity(code="TEST-01", name="Test Academics Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_academics_command_handler_flow():
    async def _run_flow():
        repo = InMemoryAcademicsRepository()
        handler = AcademicsCommandHandler(repo)

        create_cmd = CreateAcademicsCommand(code="TEST-02", name="Automated Academics")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateAcademicsCommand(id=created.id, name="Updated Academics")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Academics"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteAcademicsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_academics_serializer():
    entity = AcademicsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = AcademicsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = AcademicsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
