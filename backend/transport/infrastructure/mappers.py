"""
Transportation & GPS Fleet — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for transport.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.transport.domain.entities import TransportEntity
from backend.transport.presentation.schemas import TransportResponse

class TransportDataMapper:
    """Bidirectional persistence mapper for Transportation & GPS Fleet."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> TransportEntity:
        return TransportEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default Transportation & GPS Fleet"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: TransportEntity) -> Dict[str, Any]:
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
    def to_response_dto(entity: TransportEntity) -> TransportResponse:
        return TransportResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
