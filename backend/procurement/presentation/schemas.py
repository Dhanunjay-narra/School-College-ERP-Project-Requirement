"""
Procurement Management — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class ProcurementCreateRequest(BaseModel):
    code: str = Field(..., example="PROCUREMENT-001")
    name: str = Field(..., example="Enterprise Procurement Management Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class ProcurementResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
