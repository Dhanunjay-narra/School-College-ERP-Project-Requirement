"""
Human Resource & Recruitment — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class HrCreateRequest(BaseModel):
    code: str = Field(..., example="HR-001")
    name: str = Field(..., example="Enterprise Human Resource & Recruitment Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class HrResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
