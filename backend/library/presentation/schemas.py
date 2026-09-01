"""
Library & RFID Circulation — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class LibraryCreateRequest(BaseModel):
    code: str = Field(..., example="LIBRARY-001")
    name: str = Field(..., example="Enterprise Library & RFID Circulation Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class LibraryResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
