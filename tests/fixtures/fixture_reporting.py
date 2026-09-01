"""
Pytest Fixtures for Universal Enterprise Reporting (reporting).
"""
import pytest
from backend.reporting.domain.entities import ReportingEntity

@pytest.fixture
def sample_reporting_entity() -> ReportingEntity:
    return ReportingEntity(
        id="REPO-TEST-01",
        code="REPO-SAMPLE",
        name="Sample Universal Enterprise Reporting Entity for Pytest Verification",
        status="ACTIVE"
    )
