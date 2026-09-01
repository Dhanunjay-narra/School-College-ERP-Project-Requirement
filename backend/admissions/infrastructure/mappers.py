"""
Admissions CRM & Merit Engine — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for admissions.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.admissions.domain.entities import AdmissionsEntity
from backend.admissions.presentation.schemas import AdmissionsResponse

class AdmissionsDataMapper:
    """Bidirectional persistence mapper for Admissions CRM & Merit Engine."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> AdmissionsEntity:
        return AdmissionsEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default Admissions CRM & Merit Engine"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: AdmissionsEntity) -> Dict[str, Any]:
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
    def to_response_dto(entity: AdmissionsEntity) -> AdmissionsResponse:
        return AdmissionsResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
