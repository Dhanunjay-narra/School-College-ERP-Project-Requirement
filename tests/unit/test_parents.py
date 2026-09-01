"""
Unit Test Suite for Parent & Guardian Management (parents).
"""
import pytest
import asyncio
from datetime import datetime
from backend.parents.domain.entities import ParentsEntity
from backend.parents.application.commands import CreateParentsCommand, UpdateParentsCommand, DeleteParentsCommand
from backend.parents.application.handlers import ParentsCommandHandler
from backend.parents.infrastructure.repositories import InMemoryParentsRepository
from backend.parents.presentation.serializers import ParentsSerializer

def test_parents_entity_creation():
    entity = ParentsEntity(code="TEST-01", name="Test Parents Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_parents_command_handler_flow():
    async def _run_flow():
        repo = InMemoryParentsRepository()
        handler = ParentsCommandHandler(repo)

        create_cmd = CreateParentsCommand(code="TEST-02", name="Automated Parents")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateParentsCommand(id=created.id, name="Updated Parents")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Parents"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteParentsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_parents_serializer():
    entity = ParentsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = ParentsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = ParentsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
