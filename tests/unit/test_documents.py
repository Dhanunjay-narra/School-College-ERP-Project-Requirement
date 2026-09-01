"""
Unit Test Suite for Document Management & Signatures (documents).
"""
import pytest
import asyncio
from datetime import datetime
from backend.documents.domain.entities import DocumentsEntity
from backend.documents.application.commands import CreateDocumentsCommand, UpdateDocumentsCommand, DeleteDocumentsCommand
from backend.documents.application.handlers import DocumentsCommandHandler
from backend.documents.infrastructure.repositories import InMemoryDocumentsRepository
from backend.documents.presentation.serializers import DocumentsSerializer

def test_documents_entity_creation():
    entity = DocumentsEntity(code="TEST-01", name="Test Documents Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_documents_command_handler_flow():
    async def _run_flow():
        repo = InMemoryDocumentsRepository()
        handler = DocumentsCommandHandler(repo)

        create_cmd = CreateDocumentsCommand(code="TEST-02", name="Automated Documents")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = UpdateDocumentsCommand(id=created.id, name="Updated Documents")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated Documents"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(DeleteDocumentsCommand(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_documents_serializer():
    entity = DocumentsEntity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = DocumentsSerializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = DocumentsSerializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
