"""
Repository Test Suite for Accreditation & Regulatory Compliance (compliance).
"""
import pytest
import asyncio
from backend.compliance.domain.entities import ComplianceEntity
from backend.compliance.infrastructure.repositories import InMemoryComplianceRepository

def test_compliance_repository_crud():
    async def _run():
        repo = InMemoryComplianceRepository()
        
        # Save entity
        entity = ComplianceEntity(code="R-TEST", name="Repository Test Accreditation & Regulatory Compliance", status="ACTIVE")
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
