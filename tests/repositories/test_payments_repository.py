"""
Repository Test Suite for Payment Abstraction Gateway (payments).
"""
import pytest
import asyncio
from backend.payments.domain.entities import PaymentsEntity
from backend.payments.infrastructure.repositories import InMemoryPaymentsRepository

def test_payments_repository_crud():
    async def _run():
        repo = InMemoryPaymentsRepository()
        
        # Save entity
        entity = PaymentsEntity(code="R-TEST", name="Repository Test Payment Abstraction Gateway", status="ACTIVE")
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
