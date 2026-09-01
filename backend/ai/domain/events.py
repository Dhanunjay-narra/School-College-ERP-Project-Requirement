"""
AI/ML Predictive Intelligence — Domain Events.
"""
from backend.core.events import DomainEvent
from typing import Dict, Any

class AiCreatedEvent(DomainEvent):
    def __init__(self, aggregate_id: str, tenant_id: str, payload: Dict[str, Any]):
        super().__init__(
            event_type="ai.created",
            aggregate_id=aggregate_id,
            tenant_id=tenant_id,
            payload=payload
        )

class AiUpdatedEvent(DomainEvent):
    def __init__(self, aggregate_id: str, tenant_id: str, payload: Dict[str, Any]):
        super().__init__(
            event_type="ai.updated",
            aggregate_id=aggregate_id,
            tenant_id=tenant_id,
            payload=payload
        )
