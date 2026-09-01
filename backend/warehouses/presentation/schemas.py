"""
Multi-Store Warehouse Management — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class WarehousesCreateRequest(BaseModel):
    code: str = Field(..., example="WAREHOUSES-001")
    name: str = Field(..., example="Enterprise Multi-Store Warehouse Management Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class WarehousesResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
