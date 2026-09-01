"""
Admissions CRM & Merit Engine — Domain Events.
"""
from backend.core.events import DomainEvent
from typing import Dict, Any

class AdmissionsCreatedEvent(DomainEvent):
    def __init__(self, aggregate_id: str, tenant_id: str, payload: Dict[str, Any]):
        super().__init__(
            event_type="admissions.created",
            aggregate_id=aggregate_id,
            tenant_id=tenant_id,
            payload=payload
        )

class AdmissionsUpdatedEvent(DomainEvent):
    def __init__(self, aggregate_id: str, tenant_id: str, payload: Dict[str, Any]):
        super().__init__(
            event_type="admissions.updated",
            aggregate_id=aggregate_id,
            tenant_id=tenant_id,
            payload=payload
        )
