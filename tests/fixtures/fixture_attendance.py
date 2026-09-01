"""
Pytest Fixtures for Smart Attendance Engine (attendance).
"""
import pytest
from backend.attendance.domain.entities import AttendanceEntity

@pytest.fixture
def sample_attendance_entity() -> AttendanceEntity:
    return AttendanceEntity(
        id="ATTE-TEST-01",
        code="ATTE-SAMPLE",
        name="Sample Smart Attendance Engine Entity for Pytest Verification",
        status="ACTIVE"
    )
