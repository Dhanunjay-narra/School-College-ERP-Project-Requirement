"""
Pytest Fixtures for Examinations & Grading (examinations).
"""
import pytest
from backend.examinations.domain.entities import ExaminationsEntity

@pytest.fixture
def sample_examinations_entity() -> ExaminationsEntity:
    return ExaminationsEntity(
        id="EXAM-TEST-01",
        code="EXAM-SAMPLE",
        name="Sample Examinations & Grading Entity for Pytest Verification",
        status="ACTIVE"
    )
