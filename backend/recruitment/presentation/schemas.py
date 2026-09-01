"""
Applicant Tracking System — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class RecruitmentCreateRequest(BaseModel):
    code: str = Field(..., example="RECRUITMENT-001")
    name: str = Field(..., example="Enterprise Applicant Tracking System Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class RecruitmentResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
