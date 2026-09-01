"""
Identity & Access Management — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for identity.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.identity.domain.entities import IdentityEntity
from backend.identity.presentation.schemas import IdentityResponse

class IdentityDataMapper:
    """Bidirectional persistence mapper for Identity & Access Management."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> IdentityEntity:
        return IdentityEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default Identity & Access Management"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: IdentityEntity) -> Dict[str, Any]:
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
    def to_response_dto(entity: IdentityEntity) -> IdentityResponse:
        return IdentityResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
