"""
Domain Event Broker and Event Bus Architecture.
Supports decoupled asynchronous domain event publishing and subscription.
"""
import asyncio
import json
import logging
import uuid
from datetime import datetime
from typing import Dict, List, Callable, Any, Type, Awaitable
from pydantic import BaseModel, Field

logger = logging.getLogger("erp.events")

class DomainEvent(BaseModel):
    """Base domain event class with event metadata."""
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    event_type: str
    aggregate_id: str
    tenant_id: str = "default_institution"
    occurred_at: datetime = Field(default_factory=datetime.utcnow)
    payload: Dict[str, Any] = Field(default_factory=dict)
    version: int = 1

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

EventHandler = Callable[[DomainEvent], Awaitable[None]]

class EventBroker:
    """Central event broker for in-process or distributed event delivery."""
    def __init__(self):
        self._handlers: Dict[str, List[EventHandler]] = {}
        self._event_history: List[DomainEvent] = []

    def subscribe(self, event_type: str, handler: EventHandler):
        """Register an async event listener."""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)
        logger.info(f"Registered subscriber for event: {event_type}")

    async def publish(self, event: DomainEvent):
        """Dispatch domain event to all registered listeners asynchronously."""
        self._event_history.append(event)
        logger.info(f"Publishing domain event: {event.event_type} (ID: {event.event_id}) for aggregate: {event.aggregate_id}")
        
        handlers = self._handlers.get(event.event_type, [])
        handlers += self._handlers.get("*", [])  # Global listeners

        for handler in handlers:
            try:
                # Run handler asynchronously in event loop
                asyncio.create_task(self._safe_execute(handler, event))
            except Exception as ex:
                logger.error(f"Error launching handler for {event.event_type}: {str(ex)}")

    async def _safe_execute(self, handler: EventHandler, event: DomainEvent):
        try:
            await handler(event)
        except Exception as ex:
            logger.error(f"Handler execution failed for event {event.event_type}: {str(ex)}", exc_info=True)

    def get_history(self) -> List[DomainEvent]:
        return self._event_history

event_bus = EventBroker()
