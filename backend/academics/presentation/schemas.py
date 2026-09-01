"""
Academic Structure & Timetable — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class AcademicsCreateRequest(BaseModel):
    code: str = Field(..., example="ACADEMICS-001")
    name: str = Field(..., example="Enterprise Academic Structure & Timetable Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class AcademicsResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
