"""
Universal Multi-Channel Notifications — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for communication.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.communication.domain.entities import CommunicationEntity
from backend.communication.presentation.schemas import CommunicationResponse

class CommunicationDataMapper:
    """Bidirectional persistence mapper for Universal Multi-Channel Notifications."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> CommunicationEntity:
        return CommunicationEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default Universal Multi-Channel Notifications"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: CommunicationEntity) -> Dict[str, Any]:
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
    def to_response_dto(entity: CommunicationEntity) -> CommunicationResponse:
        return CommunicationResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
