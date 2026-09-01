"""
Admissions CRM & Merit Engine — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class AdmissionsCreateRequest(BaseModel):
    code: str = Field(..., example="ADMISSIONS-001")
    name: str = Field(..., example="Enterprise Admissions CRM & Merit Engine Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class AdmissionsResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
