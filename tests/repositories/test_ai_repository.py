"""
Repository Test Suite for AI/ML Predictive Intelligence (ai).
"""
import pytest
import asyncio
from backend.ai.domain.entities import AiEntity
from backend.ai.infrastructure.repositories import InMemoryAiRepository

def test_ai_repository_crud():
    async def _run():
        repo = InMemoryAiRepository()
        
        # Save entity
        entity = AiEntity(code="R-TEST", name="Repository Test AI/ML Predictive Intelligence", status="ACTIVE")
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
