"""
Institutional CRM & Admissions Leads — Domain Search Criteria & Specification Filter Builder.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime

class CrmCriteria:
    """Encapsulates multi-attribute filtering criteria for Institutional CRM & Admissions Leads."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self.status_in: List[str] = []
        self.search_query: Optional[str] = None
        self.created_after: Optional[datetime] = None
        self.created_before: Optional[datetime] = None
        self.metadata_filters: Dict[str, Any] = {}

    def with_status(self, *statuses: str) -> "CrmCriteria":
        self.status_in.extend([s.upper() for s in statuses])
        return self

    def with_search(self, term: Optional[str]) -> "CrmCriteria":
        self.search_query = term
        return self

    def with_created_range(self, start: Optional[datetime], end: Optional[datetime]) -> "CrmCriteria":
        self.created_after = start
        self.created_before = end
        return self

    def with_metadata_key(self, key: str, value: Any) -> "CrmCriteria":
        self.metadata_filters[key] = value
        return self
