"""
Pytest Fixtures for Multi-Store Warehouse Management (warehouses).
"""
import pytest
from backend.warehouses.domain.entities import WarehousesEntity

@pytest.fixture
def sample_warehouses_entity() -> WarehousesEntity:
    return WarehousesEntity(
        id="WARE-TEST-01",
        code="WARE-SAMPLE",
        name="Sample Multi-Store Warehouse Management Entity for Pytest Verification",
        status="ACTIVE"
    )
