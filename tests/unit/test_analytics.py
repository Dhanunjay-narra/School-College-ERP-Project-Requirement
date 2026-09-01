"""
Unit Test Suite for BI & Institutional Analytics (analytics).
"""
import pytest
import asyncio
from datetime import datetime
from backend.analytics.domain.entities import AnalyticsEntity
from backend.analytics.application.commands import CreateAnalyticsCommand, UpdateAnalyticsCommand, DeleteAnalyticsCommand
from backend.analytics.application.handlers import AnalyticsCommandHandler
from backend.analytics.infrastructure.repositories import InMemoryAnalyticsRepository
from backend.analytics.presentation.serializers import AnalyticsSerializer

def test_analytics_entity_creation():
    entity = AnalyticsEntity(code="TEST-01", name="Test Analytics Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_analytics_command_handler_flow():
    async def _run_flow():
        repo = InMemoryAnalyticsRepository()
        handler = AnalyticsCommandHandler(repo)

        create_cmd = CreateAnalyticsCommand(code="TEST-02", name="Automated Analytics")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateAnalyticsCommand(id=created.id, name="Updated Analytics")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Analytics"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteAnalyticsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_analytics_serializer():
    entity = AnalyticsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = AnalyticsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = AnalyticsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
