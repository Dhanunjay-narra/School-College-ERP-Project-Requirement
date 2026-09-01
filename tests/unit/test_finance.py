"""
Unit Test Suite for Finance & General Ledger (finance).
"""
import pytest
import asyncio
from datetime import datetime
from backend.finance.domain.entities import FinanceEntity
from backend.finance.application.commands import CreateFinanceCommand, UpdateFinanceCommand, DeleteFinanceCommand
from backend.finance.application.handlers import FinanceCommandHandler
from backend.finance.infrastructure.repositories import InMemoryFinanceRepository
from backend.finance.presentation.serializers import FinanceSerializer

def test_finance_entity_creation():
    entity = FinanceEntity(code="TEST-01", name="Test Finance Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_finance_command_handler_flow():
    async def _run_flow():
        repo = InMemoryFinanceRepository()
        handler = FinanceCommandHandler(repo)

        create_cmd = CreateFinanceCommand(code="TEST-02", name="Automated Finance")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateFinanceCommand(id=created.id, name="Updated Finance")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Finance"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteFinanceCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_finance_serializer():
    entity = FinanceEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = FinanceSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = FinanceSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
