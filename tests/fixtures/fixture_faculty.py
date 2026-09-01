"""
Pytest Fixtures for Faculty & Workload Management (faculty).
"""
import pytest
from backend.faculty.domain.entities import FacultyEntity

@pytest.fixture
def sample_faculty_entity() -> FacultyEntity:
    return FacultyEntity(
        id="FACU-TEST-01",
        code="FACU-SAMPLE",
        name="Sample Faculty & Workload Management Entity for Pytest Verification",
        status="ACTIVE"
    )
