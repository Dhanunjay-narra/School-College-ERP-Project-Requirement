"""
Unit Test Suite for Library & RFID Circulation (library).
"""
import pytest
import asyncio
from datetime import datetime
from backend.library.domain.entities import LibraryEntity
from backend.library.application.commands import CreateLibraryCommand, UpdateLibraryCommand, DeleteLibraryCommand
from backend.library.application.handlers import LibraryCommandHandler
from backend.library.infrastructure.repositories import InMemoryLibraryRepository
from backend.library.presentation.serializers import LibrarySerializer

def test_library_entity_creation():
    entity = LibraryEntity(code="TEST-01", name="Test Library Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_library_command_handler_flow():
    async def _run_flow():
        repo = InMemoryLibraryRepository()
        handler = LibraryCommandHandler(repo)

        create_cmd = CreateLibraryCommand(code="TEST-02", name="Automated Library")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateLibraryCommand(id=created.id, name="Updated Library")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Library"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteLibraryCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_library_serializer():
    entity = LibraryEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = LibrarySerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = LibrarySerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
