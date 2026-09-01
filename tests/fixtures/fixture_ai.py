"""
Pytest Fixtures for AI/ML Predictive Intelligence (ai).
"""
import pytest
from backend.ai.domain.entities import AiEntity

@pytest.fixture
def sample_ai_entity() -> AiEntity:
    return AiEntity(
        id="AI-TEST-01",
        code="AI-SAMPLE",
        name="Sample AI/ML Predictive Intelligence Entity for Pytest Verification",
        status="ACTIVE"
    )
