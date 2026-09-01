"""
Document Management & Signatures — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class DocumentsCreateRequest(BaseModel):
    code: str = Field(..., example="DOCUMENTS-001")
    name: str = Field(..., example="Enterprise Document Management & Signatures Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class DocumentsResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
