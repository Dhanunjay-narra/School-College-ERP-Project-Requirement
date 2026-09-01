"""
Pytest Fixtures for Configurable Workflow Engine (workflows).
"""
import pytest
from backend.workflows.domain.entities import WorkflowsEntity

@pytest.fixture
def sample_workflows_entity() -> WorkflowsEntity:
    return WorkflowsEntity(
        id="WORK-TEST-01",
        code="WORK-SAMPLE",
        name="Sample Configurable Workflow Engine Entity for Pytest Verification",
        status="ACTIVE"
    )
