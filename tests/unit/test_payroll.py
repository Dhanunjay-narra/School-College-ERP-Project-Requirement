"""
Unit Test Suite for Integrated Payroll Engine (payroll).
"""
import pytest
import asyncio
from datetime import datetime
from backend.payroll.domain.entities import PayrollEntity
from backend.payroll.application.commands import CreatePayrollCommand, UpdatePayrollCommand, DeletePayrollCommand
from backend.payroll.application.handlers import PayrollCommandHandler
from backend.payroll.infrastructure.repositories import InMemoryPayrollRepository
from backend.payroll.presentation.serializers import PayrollSerializer

def test_payroll_entity_creation():
    entity = PayrollEntity(code="TEST-01", name="Test Payroll Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_payroll_command_handler_flow():
    async def _run_flow():
        repo = InMemoryPayrollRepository()
        handler = PayrollCommandHandler(repo)

        create_cmd = CreatePayrollCommand(code="TEST-02", name="Automated Payroll")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdatePayrollCommand(id=created.id, name="Updated Payroll")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Payroll"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeletePayrollCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_payroll_serializer():
    entity = PayrollEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = PayrollSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = PayrollSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
