"""
Payment Abstraction Gateway — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class PaymentsCreateRequest(BaseModel):
    code: str = Field(..., example="PAYMENTS-001")
    name: str = Field(..., example="Enterprise Payment Abstraction Gateway Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class PaymentsResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
