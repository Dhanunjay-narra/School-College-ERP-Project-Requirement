"""
Pytest Fixtures for Alumni Network & Relations (alumni).
"""
import pytest
from backend.alumni.domain.entities import AlumniEntity

@pytest.fixture
def sample_alumni_entity() -> AlumniEntity:
    return AlumniEntity(
        id="ALUM-TEST-01",
        code="ALUM-SAMPLE",
        name="Sample Alumni Network & Relations Entity for Pytest Verification",
        status="ACTIVE"
    )
