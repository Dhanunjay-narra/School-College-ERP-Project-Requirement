"""
Unit Test Suite for Admissions CRM & Merit Engine (admissions).
"""
import pytest
import asyncio
from datetime import datetime
from backend.admissions.domain.entities import AdmissionsEntity
from backend.admissions.application.commands import CreateAdmissionsCommand, UpdateAdmissionsCommand, DeleteAdmissionsCommand
from backend.admissions.application.handlers import AdmissionsCommandHandler
from backend.admissions.infrastructure.repositories import InMemoryAdmissionsRepository
from backend.admissions.presentation.serializers import AdmissionsSerializer

def test_admissions_entity_creation():
    entity = AdmissionsEntity(code="TEST-01", name="Test Admissions Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_admissions_command_handler_flow():
    async def _run_flow():
        repo = InMemoryAdmissionsRepository()
        handler = AdmissionsCommandHandler(repo)

        create_cmd = CreateAdmissionsCommand(code="TEST-02", name="Automated Admissions")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateAdmissionsCommand(id=created.id, name="Updated Admissions")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Admissions"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteAdmissionsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_admissions_serializer():
    entity = AdmissionsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = AdmissionsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = AdmissionsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
