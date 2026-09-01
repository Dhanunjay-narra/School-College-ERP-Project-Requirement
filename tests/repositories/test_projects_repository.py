"""
Repository Test Suite for Campus Infrastructure Projects (projects).
"""
import pytest
import asyncio
from backend.projects.domain.entities import ProjectsEntity
from backend.projects.infrastructure.repositories import InMemoryProjectsRepository

def test_projects_repository_crud():
    async def _run():
        repo = InMemoryProjectsRepository()
        
        # Save entity
        entity = ProjectsEntity(code="R-TEST", name="Repository Test Campus Infrastructure Projects", status="ACTIVE")
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
