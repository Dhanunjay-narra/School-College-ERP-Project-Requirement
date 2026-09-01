"""
Immutable Audit Logging — Fluent Aggregate Factory & Builder.
Constructs valid Audit aggregate roots with invariant enforcement.
"""
from typing import Dict, Any, Optional
from datetime import datetime
import uuid
from backend.audit.domain.entities import AuditEntity
from backend.core.exceptions import ValidationException

class AuditFactory:
    """Factory builder for Immutable Audit Logging aggregate roots."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self._code: Optional[str] = None
        self._name: Optional[str] = None
        self._status: str = "ACTIVE"
        self._metadata: Dict[str, Any] = {}

    def set_code(self, code: str) -> "AuditFactory":
        self._code = code.strip().upper()
        return self

    def set_name(self, name: str) -> "AuditFactory":
        self._name = name.strip()
        return self

    def set_status(self, status: str) -> "AuditFactory":
        self._status = status.strip().upper()
        return self

    def add_metadata(self, key: str, value: Any) -> "AuditFactory":
        self._metadata[key] = value
        return self

    def build(self) -> AuditEntity:
        if not self._code:
            raise ValidationException("Cannot construct Audit: Unique code is mandatory.")
        if not self._name:
            raise ValidationException("Cannot construct Audit: Entity name is mandatory.")

        return AuditEntity(
            id=str(uuid.uuid4()),
            tenant_id=self.tenant_id,
            code=self._code,
            name=self._name,
            status=self._status,
            metadata=self._metadata,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
