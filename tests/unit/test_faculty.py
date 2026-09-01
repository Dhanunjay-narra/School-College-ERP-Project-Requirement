"""
Unit Test Suite for Faculty & Workload Management (faculty).
"""
import pytest
import asyncio
from datetime import datetime
from backend.faculty.domain.entities import FacultyEntity
from backend.faculty.application.commands import CreateFacultyCommand, UpdateFacultyCommand, DeleteFacultyCommand
from backend.faculty.application.handlers import FacultyCommandHandler
from backend.faculty.infrastructure.repositories import InMemoryFacultyRepository
from backend.faculty.presentation.serializers import FacultySerializer

def test_faculty_entity_creation():
    entity = FacultyEntity(code="TEST-01", name="Test Faculty Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_faculty_command_handler_flow():
    async def _run_flow():
        repo = InMemoryFacultyRepository()
        handler = FacultyCommandHandler(repo)

        create_cmd = CreateFacultyCommand(code="TEST-02", name="Automated Faculty")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateFacultyCommand(id=created.id, name="Updated Faculty")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Faculty"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteFacultyCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_faculty_serializer():
    entity = FacultyEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = FacultySerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = FacultySerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
