"""
Pytest Fixtures for Integrated Payroll Engine (payroll).
"""
import pytest
from backend.payroll.domain.entities import PayrollEntity

@pytest.fixture
def sample_payroll_entity() -> PayrollEntity:
    return PayrollEntity(
        id="PAYR-TEST-01",
        code="PAYR-SAMPLE",
        name="Sample Integrated Payroll Engine Entity for Pytest Verification",
        status="ACTIVE"
    )
