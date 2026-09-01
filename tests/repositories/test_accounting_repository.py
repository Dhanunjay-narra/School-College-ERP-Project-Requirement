"""
Repository Test Suite for Accounts Payable & Receivable (accounting).
"""
import pytest
import asyncio
from backend.accounting.domain.entities import AccountingEntity
from backend.accounting.infrastructure.repositories import InMemoryAccountingRepository

def test_accounting_repository_crud():
    async def _run():
        repo = InMemoryAccountingRepository()
        
        # Save entity
        entity = AccountingEntity(code="R-TEST", name="Repository Test Accounts Payable & Receivable", status="ACTIVE")
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
