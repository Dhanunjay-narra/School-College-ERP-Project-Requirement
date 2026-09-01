"""
Applicant Tracking System — Event Sourcing Snapshots & Event Stream Replay.
"""
from typing import List, Dict, Any, Optional
from datetime import datetime
from backend.core.events import DomainEvent

class RecruitmentSnapshot:
    def __init__(self, aggregate_id: str, version: int, state: Dict[str, Any], timestamp: Optional[datetime] = None):
        self.aggregate_id = aggregate_id
        self.version = version
        self.state = state
        self.timestamp = timestamp or datetime.utcnow()

class RecruitmentEventStream:
    """Manages ordered domain event history and snapshot state restoration for Applicant Tracking System."""

    def __init__(self, aggregate_id: str):
        self.aggregate_id = aggregate_id
        self._events: List[DomainEvent] = []
        self._latest_snapshot: Optional[RecruitmentSnapshot] = None

    def append_event(self, event: DomainEvent):
        self._events.append(event)

    def create_snapshot(self, version: int, current_state: Dict[str, Any]) -> RecruitmentSnapshot:
        self._latest_snapshot = RecruitmentSnapshot(self.aggregate_id, version, current_state)
        return self._latest_snapshot

    def get_events_since_snapshot(self) -> List[DomainEvent]:
        if not self._latest_snapshot:
            return list(self._events)
        return self._events[self._latest_snapshot.version:]
