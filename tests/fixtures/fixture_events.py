"""
Pytest Fixtures for Campus Events & Conferences (events).
"""
import pytest
from backend.events.domain.entities import EventsEntity

@pytest.fixture
def sample_events_entity() -> EventsEntity:
    return EventsEntity(
        id="EVEN-TEST-01",
        code="EVEN-SAMPLE",
        name="Sample Campus Events & Conferences Entity for Pytest Verification",
        status="ACTIVE"
    )
