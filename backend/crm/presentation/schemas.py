"""
Institutional CRM & Admissions Leads — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class CrmCreateRequest(BaseModel):
    code: str = Field(..., example="CRM-001")
    name: str = Field(..., example="Enterprise Institutional CRM & Admissions Leads Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class CrmResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
