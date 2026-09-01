"""
Unit Test Suite for Alumni Network & Relations (alumni).
"""
import pytest
import asyncio
from datetime import datetime
from backend.alumni.domain.entities import AlumniEntity
from backend.alumni.application.commands import CreateAlumniCommand, UpdateAlumniCommand, DeleteAlumniCommand
from backend.alumni.application.handlers import AlumniCommandHandler
from backend.alumni.infrastructure.repositories import InMemoryAlumniRepository
from backend.alumni.presentation.serializers import AlumniSerializer

def test_alumni_entity_creation():
    entity = AlumniEntity(code="TEST-01", name="Test Alumni Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_alumni_command_handler_flow():
    async def _run_flow():
        repo = InMemoryAlumniRepository()
        handler = AlumniCommandHandler(repo)

        create_cmd = CreateAlumniCommand(code="TEST-02", name="Automated Alumni")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateAlumniCommand(id=created.id, name="Updated Alumni")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Alumni"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteAlumniCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_alumni_serializer():
    entity = AlumniEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = AlumniSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = AlumniSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
