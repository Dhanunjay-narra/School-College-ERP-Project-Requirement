"""
Campus Workshop & Fab Lab — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class ProductionCreateRequest(BaseModel):
    code: str = Field(..., example="PRODUCTION-001")
    name: str = Field(..., example="Enterprise Campus Workshop & Fab Lab Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class ProductionResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
