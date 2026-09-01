"""
Unit Test Suite for Campus Facility Maintenance (maintenance).
"""
import pytest
import asyncio
from datetime import datetime
from backend.maintenance.domain.entities import MaintenanceEntity
from backend.maintenance.application.commands import CreateMaintenanceCommand, UpdateMaintenanceCommand, DeleteMaintenanceCommand
from backend.maintenance.application.handlers import MaintenanceCommandHandler
from backend.maintenance.infrastructure.repositories import InMemoryMaintenanceRepository
from backend.maintenance.presentation.serializers import MaintenanceSerializer

def test_maintenance_entity_creation():
    entity = MaintenanceEntity(code="TEST-01", name="Test Maintenance Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_maintenance_command_handler_flow():
    async def _run_flow():
        repo = InMemoryMaintenanceRepository()
        handler = MaintenanceCommandHandler(repo)

        create_cmd = CreateMaintenanceCommand(code="TEST-02", name="Automated Maintenance")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateMaintenanceCommand(id=created.id, name="Updated Maintenance")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Maintenance"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteMaintenanceCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_maintenance_serializer():
    entity = MaintenanceEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = MaintenanceSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = MaintenanceSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
