"""
Campus Workshop & Fab Lab — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for production.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.production.domain.entities import ProductionEntity
from backend.production.presentation.schemas import ProductionResponse

class ProductionDataMapper:
    """Bidirectional persistence mapper for Campus Workshop & Fab Lab."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> ProductionEntity:
        return ProductionEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default Campus Workshop & Fab Lab"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: ProductionEntity) -> Dict[str, Any]:
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
    def to_response_dto(entity: ProductionEntity) -> ProductionResponse:
        return ProductionResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
