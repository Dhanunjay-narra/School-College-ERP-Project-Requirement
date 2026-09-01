"""
Pytest Fixtures for LMS & Assignments (assignments).
"""
import pytest
from backend.assignments.domain.entities import AssignmentsEntity

@pytest.fixture
def sample_assignments_entity() -> AssignmentsEntity:
    return AssignmentsEntity(
        id="ASSI-TEST-01",
        code="ASSI-SAMPLE",
        name="Sample LMS & Assignments Entity for Pytest Verification",
        status="ACTIVE"
    )
