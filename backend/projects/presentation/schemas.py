"""
Campus Infrastructure Projects — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class ProjectsCreateRequest(BaseModel):
    code: str = Field(..., example="PROJECTS-001")
    name: str = Field(..., example="Enterprise Campus Infrastructure Projects Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class ProjectsResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
