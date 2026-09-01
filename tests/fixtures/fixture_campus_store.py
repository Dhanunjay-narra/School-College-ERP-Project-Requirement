"""
Pytest Fixtures for Campus Store & Cafeteria POS (campus_store).
"""
import pytest
from backend.campus_store.domain.entities import CampusStoreEntity

@pytest.fixture
def sample_campus_store_entity() -> CampusStoreEntity:
    return CampusStoreEntity(
        id="CAMP-TEST-01",
        code="CAMP-SAMPLE",
        name="Sample Campus Store & Cafeteria POS Entity for Pytest Verification",
        status="ACTIVE"
    )
