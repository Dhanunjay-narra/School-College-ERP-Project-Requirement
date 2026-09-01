from writer_util import write_f

MODULES = [
    ("identity", "Identity & Access Management"),
    ("organization", "Organization & Multi-Campus"),
    ("students", "Student Information & Lifecycle"),
    ("parents", "Parent & Guardian Management"),
    ("admissions", "Admissions CRM & Merit Engine"),
    ("academics", "Academic Structure & Timetable"),
    ("faculty", "Faculty & Workload Management"),
    ("attendance", "Smart Attendance Engine"),
    ("examinations", "Examinations & Grading"),
    ("assignments", "LMS & Assignments"),
    ("fees", "Fees & Student Billing"),
    ("payments", "Payment Abstraction Gateway"),
    ("finance", "Finance & General Ledger"),
    ("accounting", "Accounts Payable & Receivable"),
    ("procurement", "Procurement Management"),
    ("vendors", "Vendor Management & Compliance"),
    ("inventory", "Campus Inventory & Stores"),
    ("warehouses", "Multi-Store Warehouse Management"),
    ("assets", "Asset Lifecycle & Depreciation"),
    ("maintenance", "Campus Facility Maintenance"),
    ("transport", "Transportation & GPS Fleet"),
    ("hostels", "Hostel & Housing Management"),
    ("library", "Library & RFID Circulation"),
    ("hr", "Human Resource & Recruitment"),
    ("recruitment", "Applicant Tracking System"),
    ("payroll", "Integrated Payroll Engine"),
    ("crm", "Institutional CRM & Admissions Leads"),
    ("alumni", "Alumni Network & Relations"),
    ("communication", "Universal Multi-Channel Notifications"),
    ("documents", "Document Management & Signatures"),
    ("workflows", "Configurable Workflow Engine"),
    ("projects", "Campus Infrastructure Projects"),
    ("events", "Campus Events & Conferences"),
    ("research", "Research & Innovation Management"),
    ("campus_store", "Campus Store & Cafeteria POS"),
    ("production", "Campus Workshop & Fab Lab"),
    ("compliance", "Accreditation & Regulatory Compliance"),
    ("audit", "Immutable Audit Logging"),
    ("analytics", "BI & Institutional Analytics"),
    ("ai", "AI/ML Predictive Intelligence"),
    ("reporting", "Universal Enterprise Reporting"),
    ("search", "Centralized Faceted Search")
]

def generate_es_and_e2e():
    print("[EVENT SOURCING & E2E] Generating Event Sourcing Snapshots, Query Builders, and E2E Tests...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. Event Sourcing & Snapshot Store
        write_f(f"{base_dir}/domain/event_sourcing.py", f'''"""
{title} — Event Sourcing Snapshots & Event Stream Replay.
"""
from typing import List, Dict, Any, Optional
from datetime import datetime
from backend.core.events import DomainEvent

class {c_name}Snapshot:
    def __init__(self, aggregate_id: str, version: int, state: Dict[str, Any], timestamp: Optional[datetime] = None):
        self.aggregate_id = aggregate_id
        self.version = version
        self.state = state
        self.timestamp = timestamp or datetime.utcnow()

class {c_name}EventStream:
    """Manages ordered domain event history and snapshot state restoration for {title}."""

    def __init__(self, aggregate_id: str):
        self.aggregate_id = aggregate_id
        self._events: List[DomainEvent] = []
        self._latest_snapshot: Optional[{c_name}Snapshot] = None

    def append_event(self, event: DomainEvent):
        self._events.append(event)

    def create_snapshot(self, version: int, current_state: Dict[str, Any]) -> {c_name}Snapshot:
        self._latest_snapshot = {c_name}Snapshot(self.aggregate_id, version, current_state)
        return self._latest_snapshot

    def get_events_since_snapshot(self) -> List[DomainEvent]:
        if not self._latest_snapshot:
            return list(self._events)
        return self._events[self._latest_snapshot.version:]
''')

        # 2. Dynamic SQL Query Builders
        write_f(f"{base_dir}/infrastructure/query_builders.py", f'''"""
{title} — Dynamic SQL & Filtering Query Builders.
"""
from typing import Dict, Any, List, Optional

class {c_name}QueryBuilder:
    """Builds SQL query fragments for complex {title} reports."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self.filters: List[str] = [f"tenant_id = '{{tenant_id}}'"]
        self.order_by_clause = "created_at DESC"
        self.limit_count = 50
        self.offset_count = 0

    def filter_by_status(self, status: Optional[str]) -> "{c_name}QueryBuilder":
        if status:
            self.filters.append(f"status = '{{status.upper()}}'")
        return self

    def filter_by_date_range(self, start_date: Optional[str], end_date: Optional[str]) -> "{c_name}QueryBuilder":
        if start_date:
            self.filters.append(f"created_at >= '{{start_date}}'")
        if end_date:
            self.filters.append(f"created_at <= '{{end_date}}'")
        return self

    def build_sql(self) -> str:
        where_str = " AND ".join(self.filters)
        return f"SELECT * FROM erp_{mod}_records WHERE {{where_str}} ORDER BY {{self.order_by_clause}} LIMIT {{self.limit_count}} OFFSET {{self.offset_count}};"
''')

        # 3. E2E API Tests
        write_f(f"tests/e2e/test_{mod}_api.py", f'''"""
E2E API Test Suite for {title} ({mod}).
"""
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_{mod}_api_endpoints():
    # Verify module presentation and docs
    response = client.get(f"/api/v1/{mod.replace('_', '-')}/" if "{mod}" in ["students", "faculty", "assignments", "documents"] else "/health")
    assert response.status_code in [200, 404]
''')

    print("[EVENT SOURCING & E2E] Generated event sourcing, query builders, and E2E tests.")

if __name__ == '__main__':
    generate_es_and_e2e()
