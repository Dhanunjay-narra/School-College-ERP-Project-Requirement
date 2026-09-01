"""
Academic Structure & Timetable — Domain Entities.
Core enterprise domain models and business invariants for academics.
"""
import uuid
from datetime import datetime, date
from typing import List, Optional, Dict, Any

class AcademicsEntity:
    """Primary aggregate root for Academic Structure & Timetable."""
    def __init__(
        self,
        id: Optional[str] = None,
        tenant_id: str = "default_institution",
        code: str = "DEFAULT",
        name: str = "Default Academic Structure & Timetable",
        status: str = "ACTIVE",
        metadata: Optional[Dict[str, Any]] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id or str(uuid.uuid4())
        self.tenant_id = tenant_id
        self.code = code.upper()
        self.name = name
        self.status = status
        self.metadata = metadata or {}
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def update_status(self, new_status: str):
        self.status = new_status
        self.updated_at = datetime.utcnow()

    def update_metadata(self, key: str, value: Any):
        self.metadata[key] = value
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "tenant_id": self.tenant_id,
            "code": self.code,
            "name": self.name,
            "status": self.status,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
