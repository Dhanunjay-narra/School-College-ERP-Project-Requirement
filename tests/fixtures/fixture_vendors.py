"""
Pytest Fixtures for Vendor Management & Compliance (vendors).
"""
import pytest
from backend.vendors.domain.entities import VendorsEntity

@pytest.fixture
def sample_vendors_entity() -> VendorsEntity:
    return VendorsEntity(
        id="VEND-TEST-01",
        code="VEND-SAMPLE",
        name="Sample Vendor Management & Compliance Entity for Pytest Verification",
        status="ACTIVE"
    )
