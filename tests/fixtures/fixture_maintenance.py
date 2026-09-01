"""
Pytest Fixtures for Campus Facility Maintenance (maintenance).
"""
import pytest
from backend.maintenance.domain.entities import MaintenanceEntity

@pytest.fixture
def sample_maintenance_entity() -> MaintenanceEntity:
    return MaintenanceEntity(
        id="MAIN-TEST-01",
        code="MAIN-SAMPLE",
        name="Sample Campus Facility Maintenance Entity for Pytest Verification",
        status="ACTIVE"
    )
