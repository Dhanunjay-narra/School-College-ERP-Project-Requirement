"""
Parent & Guardian Management — Redis Cache Key Formatters & Invalidation Policies.
"""
from typing import Optional

class ParentsCacheKeys:
    """Standardized Redis key generator for Parent & Guardian Management."""

    PREFIX = "erp:parents"

    @classmethod
    def entity_key(cls, entity_id: str, tenant_id: str = "default_institution") -> str:
        return f"{cls.PREFIX}:{tenant_id}:entity:{entity_id}"

    @classmethod
    def list_pattern(cls, tenant_id: str = "default_institution") -> str:
        return f"{cls.PREFIX}:{tenant_id}:list:*"

    @classmethod
    def summary_key(cls, tenant_id: str = "default_institution") -> str:
        return f"{cls.PREFIX}:{tenant_id}:summary"
