"""
Pytest Fixtures for Student Information & Lifecycle (students).
"""
import pytest
from backend.students.domain.entities import StudentsEntity

@pytest.fixture
def sample_students_entity() -> StudentsEntity:
    return StudentsEntity(
        id="STUD-TEST-01",
        code="STUD-SAMPLE",
        name="Sample Student Information & Lifecycle Entity for Pytest Verification",
        status="ACTIVE"
    )
