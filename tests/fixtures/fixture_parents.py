"""
Pytest Fixtures for Parent & Guardian Management (parents).
"""
import pytest
from backend.parents.domain.entities import ParentsEntity

@pytest.fixture
def sample_parents_entity() -> ParentsEntity:
    return ParentsEntity(
        id="PARE-TEST-01",
        code="PARE-SAMPLE",
        name="Sample Parent & Guardian Management Entity for Pytest Verification",
        status="ACTIVE"
    )
