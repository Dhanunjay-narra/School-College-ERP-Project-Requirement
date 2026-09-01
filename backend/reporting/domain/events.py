"""
Universal Enterprise Reporting — Domain Events.
"""
from backend.core.events import DomainEvent
from typing import Dict, Any

class ReportingCreatedEvent(DomainEvent):
    def __init__(self, aggregate_id: str, tenant_id: str, payload: Dict[str, Any]):
        super().__init__(
            event_type="reporting.created",
            aggregate_id=aggregate_id,
            tenant_id=tenant_id,
            payload=payload
        )

class ReportingUpdatedEvent(DomainEvent):
    def __init__(self, aggregate_id: str, tenant_id: str, payload: Dict[str, Any]):
        super().__init__(
            event_type="reporting.updated",
            aggregate_id=aggregate_id,
            tenant_id=tenant_id,
            payload=payload
        )
