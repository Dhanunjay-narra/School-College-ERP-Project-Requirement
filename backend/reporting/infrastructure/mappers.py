"""
Universal Enterprise Reporting — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for reporting.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.reporting.domain.entities import ReportingEntity
from backend.reporting.presentation.schemas import ReportingResponse

class ReportingDataMapper:
    """Bidirectional persistence mapper for Universal Enterprise Reporting."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> ReportingEntity:
        return ReportingEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default Universal Enterprise Reporting"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: ReportingEntity) -> Dict[str, Any]:
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
    def to_response_dto(entity: ReportingEntity) -> ReportingResponse:
        return ReportingResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
