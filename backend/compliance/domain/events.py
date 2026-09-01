"""
Accreditation & Regulatory Compliance — Domain Events.
"""
from backend.core.events import DomainEvent
from typing import Dict, Any

class ComplianceCreatedEvent(DomainEvent):
    def __init__(self, aggregate_id: str, tenant_id: str, payload: Dict[str, Any]):
        super().__init__(
            event_type="compliance.created",
            aggregate_id=aggregate_id,
            tenant_id=tenant_id,
            payload=payload
        )

class ComplianceUpdatedEvent(DomainEvent):
    def __init__(self, aggregate_id: str, tenant_id: str, payload: Dict[str, Any]):
        super().__init__(
            event_type="compliance.updated",
            aggregate_id=aggregate_id,
            tenant_id=tenant_id,
            payload=payload
        )
