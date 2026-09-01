"""
Procurement Management — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for procurement.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.procurement.domain.entities import ProcurementEntity
from backend.procurement.presentation.schemas import ProcurementResponse

class ProcurementDataMapper:
    """Bidirectional persistence mapper for Procurement Management."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> ProcurementEntity:
        return ProcurementEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default Procurement Management"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: ProcurementEntity) -> Dict[str, Any]:
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
    def to_response_dto(entity: ProcurementEntity) -> ProcurementResponse:
        return ProcurementResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
