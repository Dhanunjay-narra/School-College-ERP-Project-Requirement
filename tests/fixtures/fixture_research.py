"""
Pytest Fixtures for Research & Innovation Management (research).
"""
import pytest
from backend.research.domain.entities import ResearchEntity

@pytest.fixture
def sample_research_entity() -> ResearchEntity:
    return ResearchEntity(
        id="RESE-TEST-01",
        code="RESE-SAMPLE",
        name="Sample Research & Innovation Management Entity for Pytest Verification",
        status="ACTIVE"
    )
