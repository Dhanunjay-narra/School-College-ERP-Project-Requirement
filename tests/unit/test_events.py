"""
Unit Test Suite for Campus Events & Conferences (events).
"""
import pytest
import asyncio
from datetime import datetime
from backend.events.domain.entities import EventsEntity
from backend.events.application.commands import CreateEventsCommand, UpdateEventsCommand, DeleteEventsCommand
from backend.events.application.handlers import EventsCommandHandler
from backend.events.infrastructure.repositories import InMemoryEventsRepository
from backend.events.presentation.serializers import EventsSerializer

def test_events_entity_creation():
    entity = EventsEntity(code="TEST-01", name="Test Events Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_events_command_handler_flow():
    async def _run_flow():
        repo = InMemoryEventsRepository()
        handler = EventsCommandHandler(repo)

        create_cmd = CreateEventsCommand(code="TEST-02", name="Automated Events")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateEventsCommand(id=created.id, name="Updated Events")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Events"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteEventsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_events_serializer():
    entity = EventsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = EventsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = EventsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
