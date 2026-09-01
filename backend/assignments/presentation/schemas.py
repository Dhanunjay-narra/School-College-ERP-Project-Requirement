"""
LMS & Assignments — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class AssignmentsCreateRequest(BaseModel):
    code: str = Field(..., example="ASSIGNMENTS-001")
    name: str = Field(..., example="Enterprise LMS & Assignments Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class AssignmentsResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
