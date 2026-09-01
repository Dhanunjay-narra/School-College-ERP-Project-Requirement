"""
Pytest Fixtures for Admissions CRM & Merit Engine (admissions).
"""
import pytest
from backend.admissions.domain.entities import AdmissionsEntity

@pytest.fixture
def sample_admissions_entity() -> AdmissionsEntity:
    return AdmissionsEntity(
        id="ADMI-TEST-01",
        code="ADMI-SAMPLE",
        name="Sample Admissions CRM & Merit Engine Entity for Pytest Verification",
        status="ACTIVE"
    )
