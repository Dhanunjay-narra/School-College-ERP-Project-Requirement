"""
Unit Test Suite for Procurement Management (procurement).
"""
import pytest
import asyncio
from datetime import datetime
from backend.procurement.domain.entities import ProcurementEntity
from backend.procurement.application.commands import CreateProcurementCommand, UpdateProcurementCommand, DeleteProcurementCommand
from backend.procurement.application.handlers import ProcurementCommandHandler
from backend.procurement.infrastructure.repositories import InMemoryProcurementRepository
from backend.procurement.presentation.serializers import ProcurementSerializer

def test_procurement_entity_creation():
    entity = ProcurementEntity(code="TEST-01", name="Test Procurement Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_procurement_command_handler_flow():
    async def _run_flow():
        repo = InMemoryProcurementRepository()
        handler = ProcurementCommandHandler(repo)

        create_cmd = CreateProcurementCommand(code="TEST-02", name="Automated Procurement")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateProcurementCommand(id=created.id, name="Updated Procurement")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Procurement"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteProcurementCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_procurement_serializer():
    entity = ProcurementEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = ProcurementSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = ProcurementSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
