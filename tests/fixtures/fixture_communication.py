"""
Pytest Fixtures for Universal Multi-Channel Notifications (communication).
"""
import pytest
from backend.communication.domain.entities import CommunicationEntity

@pytest.fixture
def sample_communication_entity() -> CommunicationEntity:
    return CommunicationEntity(
        id="COMM-TEST-01",
        code="COMM-SAMPLE",
        name="Sample Universal Multi-Channel Notifications Entity for Pytest Verification",
        status="ACTIVE"
    )
