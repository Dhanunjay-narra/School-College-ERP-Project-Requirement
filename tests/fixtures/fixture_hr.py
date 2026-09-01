"""
Pytest Fixtures for Human Resource & Recruitment (hr).
"""
import pytest
from backend.hr.domain.entities import HrEntity

@pytest.fixture
def sample_hr_entity() -> HrEntity:
    return HrEntity(
        id="HR-TEST-01",
        code="HR-SAMPLE",
        name="Sample Human Resource & Recruitment Entity for Pytest Verification",
        status="ACTIVE"
    )
