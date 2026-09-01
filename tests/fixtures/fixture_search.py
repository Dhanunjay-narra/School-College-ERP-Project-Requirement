"""
Pytest Fixtures for Centralized Faceted Search (search).
"""
import pytest
from backend.search.domain.entities import SearchEntity

@pytest.fixture
def sample_search_entity() -> SearchEntity:
    return SearchEntity(
        id="SEAR-TEST-01",
        code="SEAR-SAMPLE",
        name="Sample Centralized Faceted Search Entity for Pytest Verification",
        status="ACTIVE"
    )
