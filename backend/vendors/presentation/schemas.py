"""
Vendor Management & Compliance — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class VendorsCreateRequest(BaseModel):
    code: str = Field(..., example="VENDORS-001")
    name: str = Field(..., example="Enterprise Vendor Management & Compliance Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class VendorsResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
