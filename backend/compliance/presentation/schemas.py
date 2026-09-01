"""
Accreditation & Regulatory Compliance — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class ComplianceCreateRequest(BaseModel):
    code: str = Field(..., example="COMPLIANCE-001")
    name: str = Field(..., example="Enterprise Accreditation & Regulatory Compliance Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class ComplianceResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
