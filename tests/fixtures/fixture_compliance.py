"""
Pytest Fixtures for Accreditation & Regulatory Compliance (compliance).
"""
import pytest
from backend.compliance.domain.entities import ComplianceEntity

@pytest.fixture
def sample_compliance_entity() -> ComplianceEntity:
    return ComplianceEntity(
        id="COMP-TEST-01",
        code="COMP-SAMPLE",
        name="Sample Accreditation & Regulatory Compliance Entity for Pytest Verification",
        status="ACTIVE"
    )
