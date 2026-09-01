"""
Parent & Guardian Management — Domain Search Criteria & Specification Filter Builder.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime

class ParentsCriteria:
    """Encapsulates multi-attribute filtering criteria for Parent & Guardian Management."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self.status_in: List[str] = []
        self.search_query: Optional[str] = None
        self.created_after: Optional[datetime] = None
        self.created_before: Optional[datetime] = None
        self.metadata_filters: Dict[str, Any] = {}

    def with_status(self, *statuses: str) -> "ParentsCriteria":
        self.status_in.extend([s.upper() for s in statuses])
        return self

    def with_search(self, term: Optional[str]) -> "ParentsCriteria":
        self.search_query = term
        return self

    def with_created_range(self, start: Optional[datetime], end: Optional[datetime]) -> "ParentsCriteria":
        self.created_after = start
        self.created_before = end
        return self

    def with_metadata_key(self, key: str, value: Any) -> "ParentsCriteria":
        self.metadata_filters[key] = value
        return self
