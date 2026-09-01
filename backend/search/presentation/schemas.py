"""
Centralized Faceted Search — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class SearchCreateRequest(BaseModel):
    code: str = Field(..., example="SEARCH-001")
    name: str = Field(..., example="Enterprise Centralized Faceted Search Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class SearchResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
