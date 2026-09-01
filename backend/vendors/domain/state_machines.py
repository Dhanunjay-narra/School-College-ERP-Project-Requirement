"""
Vendor Management & Compliance — Finite State Machine (FSM) Transition Engine.
"""
from typing import Set, Dict, List
from backend.core.exceptions import DomainException

class VendorsStateMachine:
    """State machine coordinator for Vendor Management & Compliance."""

    STATE_INITIAL = "DRAFT"
    STATE_ACTIVE = "ACTIVE"
    STATE_SUSPENDED = "SUSPENDED"
    STATE_ARCHIVED = "ARCHIVED"

    ALLOWED_TRANSITIONS: Dict[str, Set[str]] = {
        "DRAFT": {"PENDING_APPROVAL", "ACTIVE", "ARCHIVED"},
        "PENDING_APPROVAL": {"APPROVED", "REJECTED", "DRAFT"},
        "APPROVED": {"ACTIVE", "ARCHIVED"},
        "ACTIVE": {"SUSPENDED", "INACTIVE", "ARCHIVED", "COMPLETED"},
        "SUSPENDED": {"ACTIVE", "ARCHIVED"},
        "INACTIVE": {"ACTIVE", "ARCHIVED"},
        "COMPLETED": {"ARCHIVED"},
        "ARCHIVED": set()
    }

    @classmethod
    def can_transition(cls, from_state: str, to_state: str) -> bool:
        valid_targets = cls.ALLOWED_TRANSITIONS.get(from_state.upper(), set())
        return to_state.upper() in valid_targets or from_state.upper() == to_state.upper()

    @classmethod
    def transition(cls, current_state: str, new_state: str) -> str:
        if not cls.can_transition(current_state, new_state):
            raise DomainException(f"State transition from '{current_state}' to '{new_state}' is disallowed in vendors.")
        return new_state.upper()
