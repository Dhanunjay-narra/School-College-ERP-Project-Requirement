"""
Repository Test Suite for Configurable Workflow Engine (workflows).
"""
import pytest
import asyncio
from backend.workflows.domain.entities import WorkflowsEntity
from backend.workflows.infrastructure.repositories import InMemoryWorkflowsRepository

def test_workflows_repository_crud():
    async def _run():
        repo = InMemoryWorkflowsRepository()
        
        # Save entity
        entity = WorkflowsEntity(code="R-TEST", name="Repository Test Configurable Workflow Engine", status="ACTIVE")
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
