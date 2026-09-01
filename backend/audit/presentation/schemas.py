"""
Immutable Audit Logging — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class AuditCreateRequest(BaseModel):
    code: str = Field(..., example="AUDIT-001")
    name: str = Field(..., example="Enterprise Immutable Audit Logging Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class AuditResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
