"""
Pytest Fixtures for Fees & Student Billing (fees).
"""
import pytest
from backend.fees.domain.entities import FeesEntity

@pytest.fixture
def sample_fees_entity() -> FeesEntity:
    return FeesEntity(
        id="FEES-TEST-01",
        code="FEES-SAMPLE",
        name="Sample Fees & Student Billing Entity for Pytest Verification",
        status="ACTIVE"
    )
