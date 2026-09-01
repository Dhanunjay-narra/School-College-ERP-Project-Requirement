"""
Organization & Multi-Campus — Denormalized Read Projections & Materialized Views.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.organization.domain.entities import OrganizationEntity

class OrganizationSummaryProjection:
    """Optimized read model for executive dashboards and mobile API feeds in Organization & Multi-Campus."""

    def __init__(self, entity: OrganizationEntity):
        self.entity_id = entity.id
        self.tenant_id = entity.tenant_id
        self.code = entity.code
        self.display_title = f"{entity.code} — {entity.name}"
        self.status = entity.status
        self.last_updated = entity.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    def to_json_dict(self) -> Dict[str, Any]:
        return {
            "id": self.entity_id,
            "tenant_id": self.tenant_id,
            "code": self.code,
            "title": self.display_title,
            "status": self.status,
            "last_updated": self.last_updated
        }
