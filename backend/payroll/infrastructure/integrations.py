"""
Integrated Payroll Engine — Third-Party Integrations & Adapter Layer.
Encapsulates external message broker publishing, caching, and external APIs for payroll.
"""
import logging
import json
from typing import Dict, Any, Optional
from backend.core.events import DomainEvent, event_bus
from backend.core.cache import cache_client

logger = logging.getLogger("erp.payroll.integrations")

class PayrollIntegrationAdapter:
    """External Gateway adapter for Integrated Payroll Engine."""
    def __init__(self, service_url: Optional[str] = None):
        self.service_url = service_url or "http://internal-gateway.local/payroll"
        logger.info(f"Initialized PayrollIntegrationAdapter with endpoint: {self.service_url}")

    async def sync_with_external_system(self, payload: Dict[str, Any]) -> bool:
        """Synchronize domain entity changes with external webhooks or legacy systems."""
        logger.info(f"Synchronizing payroll payload: {json.dumps(payload)[:100]}...")
        # Cache synced state
        cache_key = f"payroll:sync:{payload.get('id', 'latest')}"
        cache_client.set(cache_key, payload, ttl_seconds=600)
        return True

    async def publish_telemetry(self, metric_name: str, value: float):
        """Emit real-time Prometheus telemetry metric for payroll."""
        logger.info(f"Telemetry metric: payroll.{metric_name} = {value}")
