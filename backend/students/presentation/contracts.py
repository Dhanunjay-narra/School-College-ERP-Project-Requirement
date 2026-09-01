"""
Student Information & Lifecycle — Formal API Contracts & Validation Specifications.
Defines public API response payloads, header validation, and pagination contracts for students.
"""
from typing import Generic, TypeVar, List, Optional, Dict, Any
from pydantic import BaseModel, Field

T = TypeVar("T")

class StudentsContractRequest(BaseModel):
    """Client mutation contract payload for Student Information & Lifecycle."""
    action: str = Field(..., description="Action to perform", example="CREATE_OR_UPDATE")
    payload: Dict[str, Any] = Field(..., description="Domain entity attribute dictionary")
    client_version: str = Field(default="1.0.0", description="Client SDK version")
    idempotency_key: Optional[str] = Field(None, description="Unique UUID for idempotent retries")

class StudentsContractResponse(BaseModel, Generic[T]):
    """Standard unified API envelope for Student Information & Lifecycle."""
    success: bool = True
    status_code: int = 200
    message: str = "Operation executed successfully"
    data: Optional[T] = None
    errors: Optional[List[Dict[str, Any]]] = None
    telemetry: Dict[str, Any] = Field(default_factory=dict)
