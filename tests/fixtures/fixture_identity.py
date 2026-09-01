"""
Pytest Fixtures for Identity & Access Management (identity).
"""
import pytest
from backend.identity.domain.entities import IdentityEntity

@pytest.fixture
def sample_identity_entity() -> IdentityEntity:
    return IdentityEntity(
        id="IDEN-TEST-01",
        code="IDEN-SAMPLE",
        name="Sample Identity & Access Management Entity for Pytest Verification",
        status="ACTIVE"
    )
