"""
BI & Institutional Analytics — Fluent Aggregate Factory & Builder.
Constructs valid Analytics aggregate roots with invariant enforcement.
"""
from typing import Dict, Any, Optional
from datetime import datetime
import uuid
from backend.analytics.domain.entities import AnalyticsEntity
from backend.core.exceptions import ValidationException

class AnalyticsFactory:
    """Factory builder for BI & Institutional Analytics aggregate roots."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self._code: Optional[str] = None
        self._name: Optional[str] = None
        self._status: str = "ACTIVE"
        self._metadata: Dict[str, Any] = {}

    def set_code(self, code: str) -> "AnalyticsFactory":
        self._code = code.strip().upper()
        return self

    def set_name(self, name: str) -> "AnalyticsFactory":
        self._name = name.strip()
        return self

    def set_status(self, status: str) -> "AnalyticsFactory":
        self._status = status.strip().upper()
        return self

    def add_metadata(self, key: str, value: Any) -> "AnalyticsFactory":
        self._metadata[key] = value
        return self

    def build(self) -> AnalyticsEntity:
        if not self._code:
            raise ValidationException("Cannot construct Analytics: Unique code is mandatory.")
        if not self._name:
            raise ValidationException("Cannot construct Analytics: Entity name is mandatory.")

        return AnalyticsEntity(
            id=str(uuid.uuid4()),
            tenant_id=self.tenant_id,
            code=self._code,
            name=self._name,
            status=self._status,
            metadata=self._metadata,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
