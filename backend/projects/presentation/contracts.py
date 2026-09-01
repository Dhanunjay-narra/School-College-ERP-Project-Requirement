"""
Campus Infrastructure Projects — Formal API Contracts & Validation Specifications.
Defines public API response payloads, header validation, and pagination contracts for projects.
"""
from typing import Generic, TypeVar, List, Optional, Dict, Any
from pydantic import BaseModel, Field

T = TypeVar("T")

class ProjectsContractRequest(BaseModel):
    """Client mutation contract payload for Campus Infrastructure Projects."""
    action: str = Field(..., description="Action to perform", example="CREATE_OR_UPDATE")
    payload: Dict[str, Any] = Field(..., description="Domain entity attribute dictionary")
    client_version: str = Field(default="1.0.0", description="Client SDK version")
    idempotency_key: Optional[str] = Field(None, description="Unique UUID for idempotent retries")

class ProjectsContractResponse(BaseModel, Generic[T]):
    """Standard unified API envelope for Campus Infrastructure Projects."""
    success: bool = True
    status_code: int = 200
    message: str = "Operation executed successfully"
    data: Optional[T] = None
    errors: Optional[List[Dict[str, Any]]] = None
    telemetry: Dict[str, Any] = Field(default_factory=dict)
