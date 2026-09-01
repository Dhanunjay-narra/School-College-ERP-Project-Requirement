"""
Campus Facility Maintenance — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for maintenance.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.maintenance.domain.entities import MaintenanceEntity
from backend.maintenance.presentation.schemas import MaintenanceResponse

class MaintenanceDataMapper:
    """Bidirectional persistence mapper for Campus Facility Maintenance."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> MaintenanceEntity:
        return MaintenanceEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default Campus Facility Maintenance"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: MaintenanceEntity) -> Dict[str, Any]:
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
    def to_response_dto(entity: MaintenanceEntity) -> MaintenanceResponse:
        return MaintenanceResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
