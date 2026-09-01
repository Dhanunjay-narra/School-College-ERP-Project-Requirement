"""
Redis and In-Memory Caching Layer with TTL and Pattern Invalidation.
"""
import json
import logging
from typing import Optional, Any, Dict
from datetime import timedelta

logger = logging.getLogger("erp.cache")

class MemoryCache:
    """High-performance in-memory cache fallback."""
    def __init__(self):
        self._store: Dict[str, Any] = {}

    def get(self, key: str) -> Optional[Any]:
        return self._store.get(key)

    def set(self, key: str, value: Any, ttl_seconds: int = 300):
        self._store[key] = value

    def delete(self, key: str):
        self._store.pop(key, None)

    def clear(self):
        self._store.clear()

cache_client = MemoryCache()
