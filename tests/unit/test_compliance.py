"""
Unit Test Suite for Accreditation & Regulatory Compliance (compliance).
"""
import pytest
import asyncio
from datetime import datetime
from backend.compliance.domain.entities import ComplianceEntity
from backend.compliance.application.commands import CreateComplianceCommand, UpdateComplianceCommand, DeleteComplianceCommand
from backend.compliance.application.handlers import ComplianceCommandHandler
from backend.compliance.infrastructure.repositories import InMemoryComplianceRepository
from backend.compliance.presentation.serializers import ComplianceSerializer

def test_compliance_entity_creation():
    entity = ComplianceEntity(code="TEST-01", name="Test Compliance Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_compliance_command_handler_flow():
    async def _run_flow():
        repo = InMemoryComplianceRepository()
        handler = ComplianceCommandHandler(repo)

        create_cmd = CreateComplianceCommand(code="TEST-02", name="Automated Compliance")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateComplianceCommand(id=created.id, name="Updated Compliance")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Compliance"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteComplianceCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_compliance_serializer():
    entity = ComplianceEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = ComplianceSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = ComplianceSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
