"""
BI & Institutional Analytics — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for analytics.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.analytics.domain.entities import AnalyticsEntity
from backend.analytics.presentation.schemas import AnalyticsResponse

class AnalyticsDataMapper:
    """Bidirectional persistence mapper for BI & Institutional Analytics."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> AnalyticsEntity:
        return AnalyticsEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default BI & Institutional Analytics"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: AnalyticsEntity) -> Dict[str, Any]:
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
    def to_response_dto(entity: AnalyticsEntity) -> AnalyticsResponse:
        return AnalyticsResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
