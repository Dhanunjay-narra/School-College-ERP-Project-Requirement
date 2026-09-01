"""
Unit Test Suite for Universal Enterprise Reporting (reporting).
"""
import pytest
import asyncio
from datetime import datetime
from backend.reporting.domain.entities import ReportingEntity
from backend.reporting.application.commands import CreateReportingCommand, UpdateReportingCommand, DeleteReportingCommand
from backend.reporting.application.handlers import ReportingCommandHandler
from backend.reporting.infrastructure.repositories import InMemoryReportingRepository
from backend.reporting.presentation.serializers import ReportingSerializer

def test_reporting_entity_creation():
    entity = ReportingEntity(code="TEST-01", name="Test Reporting Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_reporting_command_handler_flow():
    async def _run_flow():
        repo = InMemoryReportingRepository()
        handler = ReportingCommandHandler(repo)

        create_cmd = CreateReportingCommand(code="TEST-02", name="Automated Reporting")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateReportingCommand(id=created.id, name="Updated Reporting")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Reporting"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteReportingCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_reporting_serializer():
    entity = ReportingEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = ReportingSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = ReportingSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
