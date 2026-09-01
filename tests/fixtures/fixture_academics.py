"""
Pytest Fixtures for Academic Structure & Timetable (academics).
"""
import pytest
from backend.academics.domain.entities import AcademicsEntity

@pytest.fixture
def sample_academics_entity() -> AcademicsEntity:
    return AcademicsEntity(
        id="ACAD-TEST-01",
        code="ACAD-SAMPLE",
        name="Sample Academic Structure & Timetable Entity for Pytest Verification",
        status="ACTIVE"
    )
