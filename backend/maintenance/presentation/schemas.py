"""
Campus Facility Maintenance — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class MaintenanceCreateRequest(BaseModel):
    code: str = Field(..., example="MAINTENANCE-001")
    name: str = Field(..., example="Enterprise Campus Facility Maintenance Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class MaintenanceResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
