"""
Repository Test Suite for Document Management & Signatures (documents).
"""
import pytest
import asyncio
from backend.documents.domain.entities import DocumentsEntity
from backend.documents.infrastructure.repositories import InMemoryDocumentsRepository

def test_documents_repository_crud():
    async def _run():
        repo = InMemoryDocumentsRepository()
        
        # Save entity
        entity = DocumentsEntity(code="R-TEST", name="Repository Test Document Management & Signatures", status="ACTIVE")
        saved = await repo.save(entity)
        assert saved.id is not None

        # Get entity
        fetched = await repo.get_by_id(saved.id)
        assert fetched is not None
        assert fetched.code == "R-TEST"

        # List entities
        items = await repo.list_all()
        assert len(items) >= 1

        # Delete entity
        deleted = await repo.delete(saved.id)
        assert deleted is True

    asyncio.run(_run())
