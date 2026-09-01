"""
Unit Test Suite for Payment Abstraction Gateway (payments).
"""
import pytest
import asyncio
from datetime import datetime
from backend.payments.domain.entities import PaymentsEntity
from backend.payments.application.commands import CreatePaymentsCommand, UpdatePaymentsCommand, DeletePaymentsCommand
from backend.payments.application.handlers import PaymentsCommandHandler
from backend.payments.infrastructure.repositories import InMemoryPaymentsRepository
from backend.payments.presentation.serializers import PaymentsSerializer

def test_payments_entity_creation():
    entity = PaymentsEntity(code="TEST-01", name="Test Payments Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_payments_command_handler_flow():
    async def _run_flow():
        repo = InMemoryPaymentsRepository()
        handler = PaymentsCommandHandler(repo)

        create_cmd = CreatePaymentsCommand(code="TEST-02", name="Automated Payments")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdatePaymentsCommand(id=created.id, name="Updated Payments")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Payments"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeletePaymentsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_payments_serializer():
    entity = PaymentsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = PaymentsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = PaymentsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
