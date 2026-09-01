"""
Universal Multi-Channel Notifications — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class CommunicationCreateRequest(BaseModel):
    code: str = Field(..., example="COMMUNICATION-001")
    name: str = Field(..., example="Enterprise Universal Multi-Channel Notifications Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class CommunicationResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
