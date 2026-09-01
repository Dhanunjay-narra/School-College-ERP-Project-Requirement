"""
Pytest Fixtures for Procurement Management (procurement).
"""
import pytest
from backend.procurement.domain.entities import ProcurementEntity

@pytest.fixture
def sample_procurement_entity() -> ProcurementEntity:
    return ProcurementEntity(
        id="PROC-TEST-01",
        code="PROC-SAMPLE",
        name="Sample Procurement Management Entity for Pytest Verification",
        status="ACTIVE"
    )
