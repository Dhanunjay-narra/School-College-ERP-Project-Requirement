"""
Unit Test Suite for Research & Innovation Management (research).
"""
import pytest
import asyncio
from datetime import datetime
from backend.research.domain.entities import ResearchEntity
from backend.research.application.commands import CreateResearchCommand, UpdateResearchCommand, DeleteResearchCommand
from backend.research.application.handlers import ResearchCommandHandler
from backend.research.infrastructure.repositories import InMemoryResearchRepository
from backend.research.presentation.serializers import ResearchSerializer

def test_research_entity_creation():
    entity = ResearchEntity(code="TEST-01", name="Test Research Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_research_command_handler_flow():
    async def _run_flow():
        repo = InMemoryResearchRepository()
        handler = ResearchCommandHandler(repo)

        create_cmd = CreateResearchCommand(code="TEST-02", name="Automated Research")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateResearchCommand(id=created.id, name="Updated Research")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Research"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteResearchCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_research_serializer():
    entity = ResearchEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = ResearchSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = ResearchSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
