"""
Pytest Fixtures for Document Management & Signatures (documents).
"""
import pytest
from backend.documents.domain.entities import DocumentsEntity

@pytest.fixture
def sample_documents_entity() -> DocumentsEntity:
    return DocumentsEntity(
        id="DOCU-TEST-01",
        code="DOCU-SAMPLE",
        name="Sample Document Management & Signatures Entity for Pytest Verification",
        status="ACTIVE"
    )
