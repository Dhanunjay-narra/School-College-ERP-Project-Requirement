"""
Asset Lifecycle & Depreciation — Event Stream Replay & State Reconciliation Engine.
"""
from typing import List, Dict, Any, Optional
from datetime import datetime
from backend.core.events import DomainEvent
from backend.assets.domain.entities import AssetsEntity

class AssetsEventReplayEngine:
    """Reconstructs state history for Asset Lifecycle & Depreciation aggregates from immutable event logs."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id

    def replay_events(self, initial_state: AssetsEntity, events: List[DomainEvent]) -> AssetsEntity:
        state = initial_state
        for event in sorted(events, key=lambda e: e.occurred_at):
            if event.event_type.endswith(".updated"):
                for k, v in event.payload.items():
                    if hasattr(state, k):
                        setattr(state, k, v)
            elif event.event_type.endswith(".status_changed"):
                state.update_status(str(event.payload.get("new_status", state.status)))
        return state
