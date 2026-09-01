"""
Fees & Student Billing — Dynamic SQL & Filtering Query Builders.
"""
from typing import Dict, Any, List, Optional

class FeesQueryBuilder:
    """Builds SQL query fragments for complex Fees & Student Billing reports."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self.filters: List[str] = [f"tenant_id = '{tenant_id}'"]
        self.order_by_clause = "created_at DESC"
        self.limit_count = 50
        self.offset_count = 0

    def filter_by_status(self, status: Optional[str]) -> "FeesQueryBuilder":
        if status:
            self.filters.append(f"status = '{status.upper()}'")
        return self

    def filter_by_date_range(self, start_date: Optional[str], end_date: Optional[str]) -> "FeesQueryBuilder":
        if start_date:
            self.filters.append(f"created_at >= '{start_date}'")
        if end_date:
            self.filters.append(f"created_at <= '{end_date}'")
        return self

    def build_sql(self) -> str:
        where_str = " AND ".join(self.filters)
        return f"SELECT * FROM erp_fees_records WHERE {where_str} ORDER BY {self.order_by_clause} LIMIT {self.limit_count} OFFSET {self.offset_count};"
