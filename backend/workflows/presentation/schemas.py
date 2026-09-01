"""
Configurable Workflow Engine — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class WorkflowsCreateRequest(BaseModel):
    code: str = Field(..., example="WORKFLOWS-001")
    name: str = Field(..., example="Enterprise Configurable Workflow Engine Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class WorkflowsResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
