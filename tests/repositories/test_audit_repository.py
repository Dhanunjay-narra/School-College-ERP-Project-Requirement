"""
Repository Test Suite for Immutable Audit Logging (audit).
"""
import pytest
import asyncio
from backend.audit.domain.entities import AuditEntity
from backend.audit.infrastructure.repositories import InMemoryAuditRepository

def test_audit_repository_crud():
    async def _run():
        repo = InMemoryAuditRepository()
        
        # Save entity
        entity = AuditEntity(code="R-TEST", name="Repository Test Immutable Audit Logging", status="ACTIVE")
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
