"""
Pytest Fixtures for Campus Workshop & Fab Lab (production).
"""
import pytest
from backend.production.domain.entities import ProductionEntity

@pytest.fixture
def sample_production_entity() -> ProductionEntity:
    return ProductionEntity(
        id="PROD-TEST-01",
        code="PROD-SAMPLE",
        name="Sample Campus Workshop & Fab Lab Entity for Pytest Verification",
        status="ACTIVE"
    )
