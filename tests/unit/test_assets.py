"""
Unit Test Suite for Asset Lifecycle & Depreciation (assets).
"""
import pytest
import asyncio
from datetime import datetime
from backend.assets.domain.entities import AssetsEntity
from backend.assets.application.commands import CreateAssetsCommand, UpdateAssetsCommand, DeleteAssetsCommand
from backend.assets.application.handlers import AssetsCommandHandler
from backend.assets.infrastructure.repositories import InMemoryAssetsRepository
from backend.assets.presentation.serializers import AssetsSerializer

def test_assets_entity_creation():
    entity = AssetsEntity(code="TEST-01", name="Test Assets Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_assets_command_handler_flow():
    async def _run_flow():
        repo = InMemoryAssetsRepository()
        handler = AssetsCommandHandler(repo)

        create_cmd = CreateAssetsCommand(code="TEST-02", name="Automated Assets")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateAssetsCommand(id=created.id, name="Updated Assets")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Assets"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteAssetsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_assets_serializer():
    entity = AssetsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = AssetsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = AssetsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
