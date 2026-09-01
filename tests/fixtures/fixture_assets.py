"""
Pytest Fixtures for Asset Lifecycle & Depreciation (assets).
"""
import pytest
from backend.assets.domain.entities import AssetsEntity

@pytest.fixture
def sample_assets_entity() -> AssetsEntity:
    return AssetsEntity(
        id="ASSE-TEST-01",
        code="ASSE-SAMPLE",
        name="Sample Asset Lifecycle & Depreciation Entity for Pytest Verification",
        status="ACTIVE"
    )
