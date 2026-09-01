"""
Vendor Management & Compliance — Asynchronous Event Listeners & WebSocket Dispatchers.
"""
import logging
from typing import Dict, Any
from backend.core.events import DomainEvent, event_bus
from backend.core.websocket_manager import ws_manager

logger = logging.getLogger("erp.vendors.listeners")

class VendorsEventListener:
    """Subscribes to domain events in vendors and dispatches real-time WebSocket notifications."""

    @classmethod
    async def on_entity_created(cls, event: DomainEvent):
        logger.info(f"Processing created event in vendors: {event.event_id}")
        channel = f"tenant:{event.tenant_id}:vendors"
        await ws_manager.broadcast(channel, {
            "event_type": event.event_type,
            "aggregate_id": event.aggregate_id,
            "timestamp": event.occurred_at.isoformat(),
            "payload": event.payload
        })

    @classmethod
    async def on_entity_updated(cls, event: DomainEvent):
        logger.info(f"Processing updated event in vendors: {event.event_id}")
        channel = f"tenant:{event.tenant_id}:vendors"
        await ws_manager.broadcast(channel, {
            "event_type": event.event_type,
            "aggregate_id": event.aggregate_id,
            "timestamp": event.occurred_at.isoformat(),
            "payload": event.payload
        })

    @classmethod
    def register_subscribers(cls):
        event_bus.subscribe(f"vendors.created", cls.on_entity_created)
        event_bus.subscribe(f"vendors.updated", cls.on_entity_updated)
