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
    ("campus_store", "Campus Store & Cafaria POS"),
    ("production", "Campus Workshop & Fab Lab"),
    ("compliance", "Accreditation & Regulatory Compliance"),
    ("audit", "Immutable Audit Logging"),
    ("analytics", "BI & Institutional Analytics"),
    ("ai", "AI/ML Predictive Intelligence"),
    ("reporting", "Universal Enterprise Reporting"),
    ("search", "Centralized Faceted Search")
]

def generate_criteria_and_factories():
    print("[CRITERIA & FACTORIES] Generating Domain Query Criteria and Fluent Aggregate Factories for all 40 modules...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. Query Criteria Builder
        write_f(f"{base_dir}/domain/criteria.py", f'''"""
{title} — Domain Search Criteria & Specification Filter Builder.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime

class {c_name}Criteria:
    """Encapsulates multi-attribute filtering criteria for {title}."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self.status_in: List[str] = []
        self.search_query: Optional[str] = None
        self.created_after: Optional[datetime] = None
        self.created_before: Optional[datetime] = None
        self.metadata_filters: Dict[str, Any] = {{}}

    def with_status(self, *statuses: str) -> "{c_name}Criteria":
        self.status_in.extend([s.upper() for s in statuses])
        return self

    def with_search(self, term: Optional[str]) -> "{c_name}Criteria":
        self.search_query = term
        return self

    def with_created_range(self, start: Optional[datetime], end: Optional[datetime]) -> "{c_name}Criteria":
        self.created_after = start
        self.created_before = end
        return self

    def with_metadata_key(self, key: str, value: Any) -> "{c_name}Criteria":
        self.metadata_filters[key] = value
        return self
''')

        # 2. Fluent Aggregate Factory
        write_f(f"{base_dir}/domain/factories.py", f'''"""
{title} — Fluent Aggregate Factory & Builder.
Constructs valid {c_name} aggregate roots with invariant enforcement.
"""
from typing import Dict, Any, Optional
from datetime import datetime
import uuid
from backend.{mod}.domain.entities import {c_name}Entity
from backend.core.exceptions import ValidationException

class {c_name}Factory:
    """Factory builder for {title} aggregate roots."""

    def __init__(self, tenant_id: str = "default_institution"):
        self.tenant_id = tenant_id
        self._code: Optional[str] = None
        self._name: Optional[str] = None
        self._status: str = "ACTIVE"
        self._metadata: Dict[str, Any] = {{}}

    def set_code(self, code: str) -> "{c_name}Factory":
        self._code = code.strip().upper()
        return self

    def set_name(self, name: str) -> "{c_name}Factory":
        self._name = name.strip()
        return self

    def set_status(self, status: str) -> "{c_name}Factory":
        self._status = status.strip().upper()
        return self

    def add_metadata(self, key: str, value: Any) -> "{c_name}Factory":
        self._metadata[key] = value
        return self

    def build(self) -> {c_name}Entity:
        if not self._code:
            raise ValidationException("Cannot construct {c_name}: Unique code is mandatory.")
        if not self._name:
            raise ValidationException("Cannot construct {c_name}: Entity name is mandatory.")

        return {c_name}Entity(
            id=str(uuid.uuid4()),
            tenant_id=self.tenant_id,
            code=self._code,
            name=self._name,
            status=self._status,
            metadata=self._metadata,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
''')

    print("[CRITERIA & FACTORIES] Complete criteria and aggregate factories generated.")

if __name__ == '__main__':
    generate_criteria_and_factories()
