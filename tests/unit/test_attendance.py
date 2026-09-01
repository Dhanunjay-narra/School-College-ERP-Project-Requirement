"""
Unit Test Suite for Smart Attendance Engine (attendance).
"""
import pytest
import asyncio
from datetime import datetime
from backend.attendance.domain.entities import AttendanceEntity
from backend.attendance.application.commands import CreateAttendanceCommand, UpdateAttendanceCommand, DeleteAttendanceCommand
from backend.attendance.application.handlers import AttendanceCommandHandler
from backend.attendance.infrastructure.repositories import InMemoryAttendanceRepository
from backend.attendance.presentation.serializers import AttendanceSerializer

def test_attendance_entity_creation():
    entity = AttendanceEntity(code="TEST-01", name="Test Attendance Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_attendance_command_handler_flow():
    async def _run_flow():
        repo = InMemoryAttendanceRepository()
        handler = AttendanceCommandHandler(repo)

        create_cmd = CreateAttendanceCommand(code="TEST-02", name="Automated Attendance")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateAttendanceCommand(id=created.id, name="Updated Attendance")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Attendance"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteAttendanceCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_attendance_serializer():
    entity = AttendanceEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = AttendanceSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = AttendanceSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
