"""
Unit Test Suite for AI/ML Predictive Intelligence (ai).
"""
import pytest
import asyncio
from datetime import datetime
from backend.ai.domain.entities import AiEntity
from backend.ai.application.commands import CreateAiCommand, UpdateAiCommand, DeleteAiCommand
from backend.ai.application.handlers import AiCommandHandler
from backend.ai.infrastructure.repositories import InMemoryAiRepository
from backend.ai.presentation.serializers import AiSerializer

def test_ai_entity_creation():
    entity = AiEntity(code="TEST-01", name="Test Ai Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_ai_command_handler_flow():
    async def _run_flow():
        repo = InMemoryAiRepository()
        handler = AiCommandHandler(repo)

        create_cmd = CreateAiCommand(code="TEST-02", name="Automated Ai")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateAiCommand(id=created.id, name="Updated Ai")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Ai"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteAiCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_ai_serializer():
    entity = AiEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = AiSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = AiSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
