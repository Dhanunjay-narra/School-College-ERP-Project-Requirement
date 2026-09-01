"""
Repository Test Suite for LMS & Assignments (assignments).
"""
import pytest
import asyncio
from backend.assignments.domain.entities import AssignmentsEntity
from backend.assignments.infrastructure.repositories import InMemoryAssignmentsRepository

def test_assignments_repository_crud():
    async def _run():
        repo = InMemoryAssignmentsRepository()
        
        # Save entity
        entity = AssignmentsEntity(code="R-TEST", name="Repository Test LMS & Assignments", status="ACTIVE")
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
