"""
Unit Test Suite for Applicant Tracking System (recruitment).
"""
import pytest
import asyncio
from datetime import datetime
from backend.recruitment.domain.entities import RecruitmentEntity
from backend.recruitment.application.commands import CreateRecruitmentCommand, UpdateRecruitmentCommand, DeleteRecruitmentCommand
from backend.recruitment.application.handlers import RecruitmentCommandHandler
from backend.recruitment.infrastructure.repositories import InMemoryRecruitmentRepository
from backend.recruitment.presentation.serializers import RecruitmentSerializer

def test_recruitment_entity_creation():
    entity = RecruitmentEntity(code="TEST-01", name="Test Recruitment Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_recruitment_command_handler_flow():
    async def _run_flow():
        repo = InMemoryRecruitmentRepository()
        handler = RecruitmentCommandHandler(repo)

        create_cmd = CreateRecruitmentCommand(code="TEST-02", name="Automated Recruitment")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateRecruitmentCommand(id=created.id, name="Updated Recruitment")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Recruitment"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteRecruitmentCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_recruitment_serializer():
    entity = RecruitmentEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = RecruitmentSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = RecruitmentSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
