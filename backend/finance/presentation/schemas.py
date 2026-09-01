"""
Finance & General Ledger — Pydantic API Schemas.
"""
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class FinanceCreateRequest(BaseModel):
    code: str = Field(..., example="FINANCE-001")
    name: str = Field(..., example="Enterprise Finance & General Ledger Record")
    status: str = Field(default="ACTIVE")
    metadata: Optional[Dict[str, Any]] = None

class FinanceResponse(BaseModel):
    id: str
    tenant_id: str
    code: str
    name: str
    status: str
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
