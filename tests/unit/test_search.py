"""
Unit Test Suite for Centralized Faceted Search (search).
"""
import pytest
import asyncio
from datetime import datetime
from backend.search.domain.entities import SearchEntity
from backend.search.application.commands import CreateSearchCommand, UpdateSearchCommand, DeleteSearchCommand
from backend.search.application.handlers import SearchCommandHandler
from backend.search.infrastructure.repositories import InMemorySearchRepository
from backend.search.presentation.serializers import SearchSerializer

def test_search_entity_creation():
    entity = SearchEntity(code="TEST-01", name="Test Search Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_search_command_handler_flow():
    async def _run_flow():
        repo = InMemorySearchRepository()
        handler = SearchCommandHandler(repo)

        create_cmd = CreateSearchCommand(code="TEST-02", name="Automated Search")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateSearchCommand(id=created.id, name="Updated Search")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Search"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteSearchCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_search_serializer():
    entity = SearchEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = SearchSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = SearchSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
