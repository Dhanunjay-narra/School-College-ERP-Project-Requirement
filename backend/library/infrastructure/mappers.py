"""
Library & RFID Circulation — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for library.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.library.domain.entities import LibraryEntity
from backend.library.presentation.schemas import LibraryResponse

class LibraryDataMapper:
    """Bidirectional persistence mapper for Library & RFID Circulation."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> LibraryEntity:
        return LibraryEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default Library & RFID Circulation"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: LibraryEntity) -> Dict[str, Any]:
        return {
            "id": entity.id,
            "tenant_id": entity.tenant_id,
            "code": entity.code,
            "name": entity.name,
            "status": entity.status,
            "details_json": entity.metadata,
            "updated_at": datetime.utcnow()
        }

    @staticmethod
    def to_response_dto(entity: LibraryEntity) -> LibraryResponse:
        return LibraryResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
