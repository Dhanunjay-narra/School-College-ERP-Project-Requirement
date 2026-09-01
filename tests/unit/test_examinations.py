"""
Unit Test Suite for Examinations & Grading (examinations).
"""
import pytest
import asyncio
from datetime import datetime
from backend.examinations.domain.entities import ExaminationsEntity
from backend.examinations.application.commands import CreateExaminationsCommand, UpdateExaminationsCommand, DeleteExaminationsCommand
from backend.examinations.application.handlers import ExaminationsCommandHandler
from backend.examinations.infrastructure.repositories import InMemoryExaminationsRepository
from backend.examinations.presentation.serializers import ExaminationsSerializer

def test_examinations_entity_creation():
    entity = ExaminationsEntity(code="TEST-01", name="Test Examinations Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_examinations_command_handler_flow():
    async def _run_flow():
        repo = InMemoryExaminationsRepository()
        handler = ExaminationsCommandHandler(repo)

        create_cmd = CreateExaminationsCommand(code="TEST-02", name="Automated Examinations")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateExaminationsCommand(id=created.id, name="Updated Examinations")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Examinations"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteExaminationsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_examinations_serializer():
    entity = ExaminationsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = ExaminationsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = ExaminationsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
