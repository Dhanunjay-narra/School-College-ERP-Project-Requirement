"""
Identity Domain Events.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any, Optional
from backend.core.events import DomainEvent

class UserRegisteredEvent(DomainEvent):
    def __init__(self, user_id: str, email: str, role: str, tenant_id: str):
        super().__init__(
            event_type="identity.user_registered",
            aggregate_id=user_id,
            tenant_id=tenant_id,
            payload={"user_id": user_id, "email": email, "role": role}
        )

class UserLoggedInEvent(DomainEvent):
    def __init__(self, user_id: str, ip_address: str, user_agent: str, tenant_id: str):
        super().__init__(
            event_type="identity.user_logged_in",
            aggregate_id=user_id,
            tenant_id=tenant_id,
            payload={"user_id": user_id, "ip": ip_address, "user_agent": user_agent}
        )

class UserLockedOutEvent(DomainEvent):
    def __init__(self, user_id: str, reason: str, tenant_id: str):
        super().__init__(
            event_type="identity.user_locked_out",
            aggregate_id=user_id,
            tenant_id=tenant_id,
            payload={"user_id": user_id, "reason": reason}
        )
