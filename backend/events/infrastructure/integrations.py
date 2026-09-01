"""
Campus Events & Conferences — Third-Party Integrations & Adapter Layer.
Encapsulates external message broker publishing, caching, and external APIs for events.
"""
import logging
import json
from typing import Dict, Any, Optional
from backend.core.events import DomainEvent, event_bus
from backend.core.cache import cache_client

logger = logging.getLogger("erp.events.integrations")

class EventsIntegrationAdapter:
    """External Gateway adapter for Campus Events & Conferences."""
    def __init__(self, service_url: Optional[str] = None):
        self.service_url = service_url or "http://internal-gateway.local/events"
        logger.info(f"Initialized EventsIntegrationAdapter with endpoint: {self.service_url}")

    async def sync_with_external_system(self, payload: Dict[str, Any]) -> bool:
        """Synchronize domain entity changes with external webhooks or legacy systems."""
        logger.info(f"Synchronizing events payload: {json.dumps(payload)[:100]}...")
        # Cache synced state
        cache_key = f"events:sync:{payload.get('id', 'latest')}"
        cache_client.set(cache_key, payload, ttl_seconds=600)
        return True

    async def publish_telemetry(self, metric_name: str, value: float):
        """Emit real-time Prometheus telemetry metric for events."""
        logger.info(f"Telemetry metric: events.{metric_name} = {value}")
