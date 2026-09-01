"""
Pytest Fixtures for Campus Inventory & Stores (inventory).
"""
import pytest
from backend.inventory.domain.entities import InventoryEntity

@pytest.fixture
def sample_inventory_entity() -> InventoryEntity:
    return InventoryEntity(
        id="INVE-TEST-01",
        code="INVE-SAMPLE",
        name="Sample Campus Inventory & Stores Entity for Pytest Verification",
        status="ACTIVE"
    )
