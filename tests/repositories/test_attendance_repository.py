"""
Repository Test Suite for Smart Attendance Engine (attendance).
"""
import pytest
import asyncio
from backend.attendance.domain.entities import AttendanceEntity
from backend.attendance.infrastructure.repositories import InMemoryAttendanceRepository

def test_attendance_repository_crud():
    async def _run():
        repo = InMemoryAttendanceRepository()
        
        # Save entity
        entity = AttendanceEntity(code="R-TEST", name="Repository Test Smart Attendance Engine", status="ACTIVE")
        saved = await repo.save(entity)
        assert saved.id is not None

        # Get entity
        fetched = await repo.get_by_id(saved.id)
        assert fetched is not None
        assert fetched.code == "R-TEST"

        # List entities
        items = await repo.list_all()
        assert len(items) >= 1

        # Delete entity
        deleted = await repo.delete(saved.id)
        assert deleted is True

    asyncio.run(_run())
