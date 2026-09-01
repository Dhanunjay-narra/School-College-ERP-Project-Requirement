"""
Configurable Workflow Engine — CQRS Commands.
Defines immutable command structures and validations for workflows.
"""
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
from datetime import datetime
import uuid

@dataclass(frozen=True)
class CreateWorkflowsCommand:
    code: str
    name: str
    tenant_id: str = "default_institution"
    status: str = "ACTIVE"
    metadata: Dict[str, Any] = field(default_factory=dict)
    command_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass(frozen=True)
class UpdateWorkflowsCommand:
    id: str
    name: Optional[str] = None
    status: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tenant_id: str = "default_institution"
    command_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass(frozen=True)
class DeleteWorkflowsCommand:
    id: str
    tenant_id: str = "default_institution"
    reason: str = "Administrative action"
    command_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass(frozen=True)
class BatchProcessWorkflowsCommand:
    item_ids: List[str]
    action: str
    tenant_id: str = "default_institution"
    parameters: Dict[str, Any] = field(default_factory=dict)
    command_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)
