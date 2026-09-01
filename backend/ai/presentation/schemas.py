"""
AI/ML Predictive Intelligence — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class AiCreateRequest(BaseModel):
    code: str = Field(..., example="AI-001")
    name: str = Field(..., example="Enterprise AI/ML Predictive Intelligence Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class AiResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
