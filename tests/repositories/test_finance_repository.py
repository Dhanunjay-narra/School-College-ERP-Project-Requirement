"""
Repository Test Suite for Finance & General Ledger (finance).
"""
import pytest
import asyncio
from backend.finance.domain.entities import FinanceEntity
from backend.finance.infrastructure.repositories import InMemoryFinanceRepository

def test_finance_repository_crud():
    async def _run():
        repo = InMemoryFinanceRepository()
        
        # Save entity
        entity = FinanceEntity(code="R-TEST", name="Repository Test Finance & General Ledger", status="ACTIVE")
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
