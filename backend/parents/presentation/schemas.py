"""
Parent & Guardian Management — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class ParentsCreateRequest(BaseModel):
    code: str = Field(..., example="PARENTS-001")
    name: str = Field(..., example="Enterprise Parent & Guardian Management Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class ParentsResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
