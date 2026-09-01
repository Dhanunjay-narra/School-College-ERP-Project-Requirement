"""
Pytest Fixtures for Campus Infrastructure Projects (projects).
"""
import pytest
from backend.projects.domain.entities import ProjectsEntity

@pytest.fixture
def sample_projects_entity() -> ProjectsEntity:
    return ProjectsEntity(
        id="PROJ-TEST-01",
        code="PROJ-SAMPLE",
        name="Sample Campus Infrastructure Projects Entity for Pytest Verification",
        status="ACTIVE"
    )
