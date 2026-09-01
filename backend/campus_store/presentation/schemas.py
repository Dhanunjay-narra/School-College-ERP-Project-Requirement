"""
Campus Store & Cafeteria POS — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class CampusStoreCreateRequest(BaseModel):
    code: str = Field(..., example="CAMPUS_STORE-001")
    name: str = Field(..., example="Enterprise Campus Store & Cafeteria POS Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class CampusStoreResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
