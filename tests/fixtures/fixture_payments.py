"""
Pytest Fixtures for Payment Abstraction Gateway (payments).
"""
import pytest
from backend.payments.domain.entities import PaymentsEntity

@pytest.fixture
def sample_payments_entity() -> PaymentsEntity:
    return PaymentsEntity(
        id="PAYM-TEST-01",
        code="PAYM-SAMPLE",
        name="Sample Payment Abstraction Gateway Entity for Pytest Verification",
        status="ACTIVE"
    )
