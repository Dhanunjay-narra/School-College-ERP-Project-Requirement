"""
Identity & Access Management — Asynchronous Event Listeners & WebSocket Dispatchers.
"""
import logging
from typing import Dict, Any
from backend.core.events import DomainEvent, event_bus
from backend.core.websocket_manager import ws_manager

logger = logging.getLogger("erp.identity.listeners")

class IdentityEventListener:
    """Subscribes to domain events in identity and dispatches real-time WebSocket notifications."""

    @classmethod
    async def on_entity_created(cls, event: DomainEvent):
        logger.info(f"Processing created event in identity: {event.event_id}")
        channel = f"tenant:{event.tenant_id}:identity"
        await ws_manager.broadcast(channel, {
            "event_type": event.event_type,
            "aggregate_id": event.aggregate_id,
            "timestamp": event.occurred_at.isoformat(),
            "payload": event.payload
        })

    @classmethod
    async def on_entity_updated(cls, event: DomainEvent):
        logger.info(f"Processing updated event in identity: {event.event_id}")
        channel = f"tenant:{event.tenant_id}:identity"
        await ws_manager.broadcast(channel, {
            "event_type": event.event_type,
            "aggregate_id": event.aggregate_id,
            "timestamp": event.occurred_at.isoformat(),
            "payload": event.payload
        })

    @classmethod
    def register_subscribers(cls):
        event_bus.subscribe(f"identity.created", cls.on_entity_created)
        event_bus.subscribe(f"identity.updated", cls.on_entity_updated)
