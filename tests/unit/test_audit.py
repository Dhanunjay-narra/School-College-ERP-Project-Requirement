"""
Unit Test Suite for Immutable Audit Logging (audit).
"""
import pytest
import asyncio
from datetime import datetime
from backend.audit.domain.entities import AuditEntity
from backend.audit.application.commands import CreateAuditCommand, UpdateAuditCommand, DeleteAuditCommand
from backend.audit.application.handlers import AuditCommandHandler
from backend.audit.infrastructure.repositories import InMemoryAuditRepository
from backend.audit.presentation.serializers import AuditSerializer

def test_audit_entity_creation():
    entity = AuditEntity(code="TEST-01", name="Test Audit Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_audit_command_handler_flow():
    async def _run_flow():
        repo = InMemoryAuditRepository()
        handler = AuditCommandHandler(repo)

        create_cmd = CreateAuditCommand(code="TEST-02", name="Automated Audit")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateAuditCommand(id=created.id, name="Updated Audit")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Audit"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteAuditCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_audit_serializer():
    entity = AuditEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = AuditSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = AuditSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
