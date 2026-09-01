"""
Pytest Fixtures for Finance & General Ledger (finance).
"""
import pytest
from backend.finance.domain.entities import FinanceEntity

@pytest.fixture
def sample_finance_entity() -> FinanceEntity:
    return FinanceEntity(
        id="FINA-TEST-01",
        code="FINA-SAMPLE",
        name="Sample Finance & General Ledger Entity for Pytest Verification",
        status="ACTIVE"
    )
