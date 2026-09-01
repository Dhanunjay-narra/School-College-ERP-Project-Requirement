"""
Fees & Student Billing — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class FeesCreateRequest(BaseModel):
    code: str = Field(..., example="FEES-001")
    name: str = Field(..., example="Enterprise Fees & Student Billing Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class FeesResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
