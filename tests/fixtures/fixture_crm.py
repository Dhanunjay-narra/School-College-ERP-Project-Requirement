"""
Pytest Fixtures for Institutional CRM & Admissions Leads (crm).
"""
import pytest
from backend.crm.domain.entities import CrmEntity

@pytest.fixture
def sample_crm_entity() -> CrmEntity:
    return CrmEntity(
        id="CRM-TEST-01",
        code="CRM-SAMPLE",
        name="Sample Institutional CRM & Admissions Leads Entity for Pytest Verification",
        status="ACTIVE"
    )
