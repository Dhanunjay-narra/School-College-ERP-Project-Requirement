"""
Asset Lifecycle & Depreciation — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class AssetsCreateRequest(BaseModel):
    code: str = Field(..., example="ASSETS-001")
    name: str = Field(..., example="Enterprise Asset Lifecycle & Depreciation Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class AssetsResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
