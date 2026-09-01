"""
Pytest Fixtures for Applicant Tracking System (recruitment).
"""
import pytest
from backend.recruitment.domain.entities import RecruitmentEntity

@pytest.fixture
def sample_recruitment_entity() -> RecruitmentEntity:
    return RecruitmentEntity(
        id="RECR-TEST-01",
        code="RECR-SAMPLE",
        name="Sample Applicant Tracking System Entity for Pytest Verification",
        status="ACTIVE"
    )
