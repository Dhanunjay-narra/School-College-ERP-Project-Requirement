"""
BI & Institutional Analytics — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class AnalyticsCreateRequest(BaseModel):
    code: str = Field(..., example="ANALYTICS-001")
    name: str = Field(..., example="Enterprise BI & Institutional Analytics Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class AnalyticsResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
