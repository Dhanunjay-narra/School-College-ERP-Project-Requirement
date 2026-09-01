"""
Pytest Fixtures for Organization & Multi-Campus (organization).
"""
import pytest
from backend.organization.domain.entities import OrganizationEntity

@pytest.fixture
def sample_organization_entity() -> OrganizationEntity:
    return OrganizationEntity(
        id="ORGA-TEST-01",
        code="ORGA-SAMPLE",
        name="Sample Organization & Multi-Campus Entity for Pytest Verification",
        status="ACTIVE"
    )
