"""
Student Information & Lifecycle — Domain Events.
"""
from backend.core.events import DomainEvent
from typing import Dict, Any

class StudentsCreatedEvent(DomainEvent):
    def __init__(self, aggregate_id: str, tenant_id: str, payload: Dict[str, Any]):
        super().__init__(
            event_type="students.created",
            aggregate_id=aggregate_id,
            tenant_id=tenant_id,
            payload=payload
        )

class StudentsUpdatedEvent(DomainEvent):
    def __init__(self, aggregate_id: str, tenant_id: str, payload: Dict[str, Any]):
        super().__init__(
            event_type="students.updated",
            aggregate_id=aggregate_id,
            tenant_id=tenant_id,
            payload=payload
        )
