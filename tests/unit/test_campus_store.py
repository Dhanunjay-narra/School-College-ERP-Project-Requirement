"""
Unit Test Suite for Campus Store & Cafeteria POS (campus_store).
"""
import pytest
import asyncio
from datetime import datetime
from backend.campus_store.domain.entities import CampusStoreEntity
from backend.campus_store.application.commands import CreateCampusStoreCommand, UpdateCampusStoreCommand, DeleteCampusStoreCommand
from backend.campus_store.application.handlers import CampusStoreCommandHandler
from backend.campus_store.infrastructure.repositories import InMemoryCampusStoreRepository
from backend.campus_store.presentation.serializers import CampusStoreSerializer

def test_campus_store_entity_creation():
    entity = CampusStoreEntity(code="TEST-01", name="Test CampusStore Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_campus_store_command_handler_flow():
    async def _run_flow():
        repo = InMemoryCampusStoreRepository()
        handler = CampusStoreCommandHandler(repo)

        create_cmd = CreateCampusStoreCommand(code="TEST-02", name="Automated CampusStore")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateCampusStoreCommand(id=created.id, name="Updated CampusStore")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated CampusStore"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteCampusStoreCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_campus_store_serializer():
    entity = CampusStoreEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = CampusStoreSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = CampusStoreSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
