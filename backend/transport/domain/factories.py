"""
Transportation & GPS Fleet — Fluent Aggregate Factory & Builder.
Constructs valid Transport aggregate roots with invariant enforcement.
"""
from typing import Dict, Any, Optional
from datetime import datetime
import uuid
from backend.transport.domain.entities import TransportEntity
from backend.core.exceptions import ValidationException

class TransportFactory:
    """Factory builder for Transportation & GPS Fleet aggregate roots."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self._code: Optional[str] = None
        self._name: Optional[str] = None
        self._status: str = "ACTIVE"
        self._metadata: Dict[str, Any] = {}

    def set_code(self, code: str) -> "TransportFactory":
        self._code = code.strip().upper()
        return self

    def set_name(self, name: str) -> "TransportFactory":
        self._name = name.strip()
        return self

    def set_status(self, status: str) -> "TransportFactory":
        self._status = status.strip().upper()
        return self

    def add_metadata(self, key: str, value: Any) -> "TransportFactory":
        self._metadata[key] = value
        return self

    def build(self) -> TransportEntity:
        if not self._code:
            raise ValidationException("Cannot construct Transport: Unique code is mandatory.")
        if not self._name:
            raise ValidationException("Cannot construct Transport: Entity name is mandatory.")

        return TransportEntity(
            id=str(uuid.uuid4()),
            tenant_id=self.tenant_id,
            code=self._code,
            name=self._name,
            status=self._status,
            metadata=self._metadata,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
