"""
Unit Test Suite for LMS & Assignments (assignments).
"""
import pytest
import asyncio
from datetime import datetime
from backend.assignments.domain.entities import AssignmentsEntity
from backend.assignments.application.commands import CreateAssignmentsCommand, UpdateAssignmentsCommand, DeleteAssignmentsCommand
from backend.assignments.application.handlers import AssignmentsCommandHandler
from backend.assignments.infrastructure.repositories import InMemoryAssignmentsRepository
from backend.assignments.presentation.serializers import AssignmentsSerializer

def test_assignments_entity_creation():
    entity = AssignmentsEntity(code="TEST-01", name="Test Assignments Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_assignments_command_handler_flow():
    async def _run_flow():
        repo = InMemoryAssignmentsRepository()
        handler = AssignmentsCommandHandler(repo)

        create_cmd = CreateAssignmentsCommand(code="TEST-02", name="Automated Assignments")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateAssignmentsCommand(id=created.id, name="Updated Assignments")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Assignments"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteAssignmentsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_assignments_serializer():
    entity = AssignmentsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = AssignmentsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = AssignmentsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
