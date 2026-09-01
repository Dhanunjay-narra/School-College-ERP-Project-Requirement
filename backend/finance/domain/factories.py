"""
Finance & General Ledger — Fluent Aggregate Factory & Builder.
Constructs valid Finance aggregate roots with invariant enforcement.
"""
from typing import Dict, Any, Optional
from datetime import datetime
import uuid
from backend.finance.domain.entities import FinanceEntity
from backend.core.exceptions import ValidationException

class FinanceFactory:
    """Factory builder for Finance & General Ledger aggregate roots."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self._code: Optional[str] = None
        self._name: Optional[str] = None
        self._status: str = "ACTIVE"
        self._metadata: Dict[str, Any] = {}

    def set_code(self, code: str) -> "FinanceFactory":
        self._code = code.strip().upper()
        return self

    def set_name(self, name: str) -> "FinanceFactory":
        self._name = name.strip()
        return self

    def set_status(self, status: str) -> "FinanceFactory":
        self._status = status.strip().upper()
        return self

    def add_metadata(self, key: str, value: Any) -> "FinanceFactory":
        self._metadata[key] = value
        return self

    def build(self) -> FinanceEntity:
        if not self._code:
            raise ValidationException("Cannot construct Finance: Unique code is mandatory.")
        if not self._name:
            raise ValidationException("Cannot construct Finance: Entity name is mandatory.")

        return FinanceEntity(
            id=str(uuid.uuid4()),
            tenant_id=self.tenant_id,
            code=self._code,
            name=self._name,
            status=self._status,
            metadata=self._metadata,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
