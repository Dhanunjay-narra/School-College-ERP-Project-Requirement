"""
Unit Test Suite for Campus Infrastructure Projects (projects).
"""
import pytest
import asyncio
from datetime import datetime
from backend.projects.domain.entities import ProjectsEntity
from backend.projects.application.commands import CreateProjectsCommand, UpdateProjectsCommand, DeleteProjectsCommand
from backend.projects.application.handlers import ProjectsCommandHandler
from backend.projects.infrastructure.repositories import InMemoryProjectsRepository
from backend.projects.presentation.serializers import ProjectsSerializer

def test_projects_entity_creation():
    entity = ProjectsEntity(code="TEST-01", name="Test Projects Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_projects_command_handler_flow():
    async def _run_flow():
        repo = InMemoryProjectsRepository()
        handler = ProjectsCommandHandler(repo)

        create_cmd = CreateProjectsCommand(code="TEST-02", name="Automated Projects")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateProjectsCommand(id=created.id, name="Updated Projects")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Projects"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteProjectsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_projects_serializer():
    entity = ProjectsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = ProjectsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = ProjectsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
