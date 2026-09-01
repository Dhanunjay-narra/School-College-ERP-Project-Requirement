"""
Pytest Fixtures for Accounts Payable & Receivable (accounting).
"""
import pytest
from backend.accounting.domain.entities import AccountingEntity

@pytest.fixture
def sample_accounting_entity() -> AccountingEntity:
    return AccountingEntity(
        id="ACCO-TEST-01",
        code="ACCO-SAMPLE",
        name="Sample Accounts Payable & Receivable Entity for Pytest Verification",
        status="ACTIVE"
    )
