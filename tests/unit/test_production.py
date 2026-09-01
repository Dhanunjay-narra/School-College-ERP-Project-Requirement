"""
Unit Test Suite for Campus Workshop & Fab Lab (production).
"""
import pytest
import asyncio
from datetime import datetime
from backend.production.domain.entities import ProductionEntity
from backend.production.application.commands import CreateProductionCommand, UpdateProductionCommand, DeleteProductionCommand
from backend.production.application.handlers import ProductionCommandHandler
from backend.production.infrastructure.repositories import InMemoryProductionRepository
from backend.production.presentation.serializers import ProductionSerializer

def test_production_entity_creation():
    entity = ProductionEntity(code="TEST-01", name="Test Production Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_production_command_handler_flow():
    async def _run_flow():
        repo = InMemoryProductionRepository()
        handler = ProductionCommandHandler(repo)

        create_cmd = CreateProductionCommand(code="TEST-02", name="Automated Production")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateProductionCommand(id=created.id, name="Updated Production")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Production"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteProductionCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_production_serializer():
    entity = ProductionEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = ProductionSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = ProductionSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
