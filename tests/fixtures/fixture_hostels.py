"""
Pytest Fixtures for Hostel & Housing Management (hostels).
"""
import pytest
from backend.hostels.domain.entities import HostelsEntity

@pytest.fixture
def sample_hostels_entity() -> HostelsEntity:
    return HostelsEntity(
        id="HOST-TEST-01",
        code="HOST-SAMPLE",
        name="Sample Hostel & Housing Management Entity for Pytest Verification",
        status="ACTIVE"
    )
