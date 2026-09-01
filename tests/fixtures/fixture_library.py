"""
Pytest Fixtures for Library & RFID Circulation (library).
"""
import pytest
from backend.library.domain.entities import LibraryEntity

@pytest.fixture
def sample_library_entity() -> LibraryEntity:
    return LibraryEntity(
        id="LIBR-TEST-01",
        code="LIBR-SAMPLE",
        name="Sample Library & RFID Circulation Entity for Pytest Verification",
        status="ACTIVE"
    )
