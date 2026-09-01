"""
Pytest Fixtures for Immutable Audit Logging (audit).
"""
import pytest
from backend.audit.domain.entities import AuditEntity

@pytest.fixture
def sample_audit_entity() -> AuditEntity:
    return AuditEntity(
        id="AUDI-TEST-01",
        code="AUDI-SAMPLE",
        name="Sample Immutable Audit Logging Entity for Pytest Verification",
        status="ACTIVE"
    )
