"""
Campus Store & Cafeteria POS — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for campus_store.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.campus_store.domain.entities import CampusStoreEntity
from backend.campus_store.presentation.schemas import CampusStoreResponse

class CampusStoreDataMapper:
    """Bidirectional persistence mapper for Campus Store & Cafeteria POS."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> CampusStoreEntity:
        return CampusStoreEntity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default Campus Store & Cafeteria POS"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {})
        )

    @staticmethod
    def to_persistence(entity: CampusStoreEntity) -> Dict[str, Any]:
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
    def to_response_dto(entity: CampusStoreEntity) -> CampusStoreResponse:
        return CampusStoreResponse(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
