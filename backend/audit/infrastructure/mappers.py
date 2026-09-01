"""
Immutable Audit Logging — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for audit.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.audit.domain.entities import AuditEntity
from backend.audit.presentation.schemas import AuditResponse

class AuditDataMapper:
    """Bidirectional persistence mapper for Immutable Audit Logging."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> AuditEntity:
        return AuditEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default Immutable Audit Logging"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: AuditEntity) -> Dict[str, Any]:
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
    def to_response_dto(entity: AuditEntity) -> AuditResponse:
        return AuditResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
