"""
Pytest Fixtures for BI & Institutional Analytics (analytics).
"""
import pytest
from backend.analytics.domain.entities import AnalyticsEntity

@pytest.fixture
def sample_analytics_entity() -> AnalyticsEntity:
    return AnalyticsEntity(
        id="ANAL-TEST-01",
        code="ANAL-SAMPLE",
        name="Sample BI & Institutional Analytics Entity for Pytest Verification",
        status="ACTIVE"
    )
