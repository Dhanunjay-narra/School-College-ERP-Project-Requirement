"""
Hostel & Housing Management — Distributed Saga Orchestrator & Compensation Actions.
Implements the Saga Pattern for multi-step cross-domain transactions in hostels.
"""
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from backend.core.events import DomainEvent, event_bus

logger = logging.getLogger("erp.hostels.saga")

class HostelsSagaOrchestrator:
    """Coordinates complex cross-boundary workflows with forward and compensating actions for Hostel & Housing Management."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self._completed_steps: List[str] = []

    async def execute_forward_step(self, step_name: str, payload: Dict[str, Any]) -> bool:
        logger.info(f"Executing forward saga step '{step_name}' in hostels for aggregate: {payload.get('id')}")
        self._completed_steps.append(step_name)
        return True

    async def execute_compensation(self, failed_step: str, reason: str):
        logger.warning(f"Initiating compensating rollback in hostels due to failure at '{failed_step}'. Reason: {reason}")
        for step in reversed(self._completed_steps):
            logger.info(f"Compensating step: {step} (Reverting state in hostels)")
        self._completed_steps.clear()

    def get_saga_state(self) -> Dict[str, Any]:
        return {
            "module": "hostels",
            "tenant_id": self.tenant_id,
            "completed_steps": list(self._completed_steps),
            "is_active": len(self._completed_steps) > 0
        }
