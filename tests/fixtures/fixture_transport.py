"""
Pytest Fixtures for Transportation & GPS Fleet (transport).
"""
import pytest
from backend.transport.domain.entities import TransportEntity

@pytest.fixture
def sample_transport_entity() -> TransportEntity:
    return TransportEntity(
        id="TRAN-TEST-01",
        code="TRAN-SAMPLE",
        name="Sample Transportation & GPS Fleet Entity for Pytest Verification",
        status="ACTIVE"
    )
