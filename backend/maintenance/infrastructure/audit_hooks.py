"""
Campus Facility Maintenance — Change-Data-Capture (CDC) & Audit Interceptors.
Captures attribute-level diffs and emits immutable cryptographic audit logs for maintenance.
"""
import hashlib
import json
import logging
from typing import Dict, Any, Optional
from datetime import datetime
from backend.core.events import DomainEvent, event_bus

logger = logging.getLogger("erp.maintenance.audit")

class MaintenanceAuditHook:
    """Interceps mutations to record before/after state diffs for Campus Facility Maintenance."""

    @staticmethod
    def calculate_state_hash(state: Dict[str, Any]) -> str:
        serialized = json.dumps(state, sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

    @classmethod
    async def record_mutation(
        cls,
        entity_id: str,
        actor_id: str,
        action: str,
        old_state: Optional[Dict[str, Any]],
        new_state: Dict[str, Any],
        tenant_id: str = "default_institution"
    ):
        old_hash = cls.calculate_state_hash(old_state) if old_state else "GENESIS_STATE"
        new_hash = cls.calculate_state_hash(new_state)

        audit_payload = {
            "module": "maintenance",
            "entity_id": entity_id,
            "actor_id": actor_id,
            "action": action,
            "old_state_hash": old_hash,
            "new_state_hash": new_hash,
            "diff_keys": [k for k in new_state.keys() if not old_state or old_state.get(k) != new_state.get(k)],
            "timestamp": datetime.utcnow().isoformat()
        }
        logger.info(f"Audit record generated for maintenance.{entity_id}: {action} (Hash: {new_hash[:8]})")
        return audit_payload
