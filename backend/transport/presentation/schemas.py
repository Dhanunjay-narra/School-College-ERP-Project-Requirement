"""
Transportation & GPS Fleet — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class TransportCreateRequest(BaseModel):
    code: str = Field(..., example="TRANSPORT-001")
    name: str = Field(..., example="Enterprise Transportation & GPS Fleet Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class TransportResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
