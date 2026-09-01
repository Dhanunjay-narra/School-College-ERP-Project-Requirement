"""
Smart Attendance Engine — Domain Search Criteria & Specification Filter Builder.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime

class AttendanceCriteria:
    """Encapsulates multi-attribute filtering criteria for Smart Attendance Engine."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self.status_in: List[str] = []
        self.search_query: Optional[str] = None
        self.created_after: Optional[datetime] = None
        self.created_before: Optional[datetime] = None
        self.metadata_filters: Dict[str, Any] = {}

    def with_status(self, *statuses: str) -> "AttendanceCriteria":
        self.status_in.extend([s.upper() for s in statuses])
        return self

    def with_search(self, term: Optional[str]) -> "AttendanceCriteria":
        self.search_query = term
        return self

    def with_created_range(self, start: Optional[datetime], end: Optional[datetime]) -> "AttendanceCriteria":
        self.created_after = start
        self.created_before = end
        return self

    def with_metadata_key(self, key: str, value: Any) -> "AttendanceCriteria":
        self.metadata_filters[key] = value
        return self
