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

def generate_projections_and_indexers():
    print("[PROJECTIONS & INDEXERS] Generating Domain Projections and In-Memory Indexers for all 40 modules...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. Denormalized Read Projections
        write_f(f"{base_dir}/domain/projections.py", f'''"""
{title} — Denormalized Read Projections & Materialized Views.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.{mod}.domain.entities import {c_name}Entity

class {c_name}SummaryProjection:
    """Optimized read model for executive dashboards and mobile API feeds in {title}."""

    def __init__(self, entity: {c_name}Entity):
        self.entity_id = entity.id
        self.tenant_id = entity.tenant_id
        self.code = entity.code
        self.display_title = f"{{entity.code}} — {{entity.name}}"
        self.status = entity.status
        self.last_updated = entity.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    def to_json_dict(self) -> Dict[str, Any]:
        return {{
            "id": self.entity_id,
            "tenant_id": self.tenant_id,
            "code": self.code,
            "title": self.display_title,
            "status": self.status,
            "last_updated": self.last_updated
        }}
''')

        # 2. In-Memory Indexers
        write_f(f"{base_dir}/infrastructure/indexers.py", f'''"""
{title} — In-Memory Secondary Indexer.
Enables sub-millisecond lookup by code, status, and tenant in {mod}.
"""
from typing import Dict, List, Set, Optional
from backend.{mod}.domain.entities import {c_name}Entity

class {c_name}MemoryIndexer:
    """Secondary index manager for {title}."""

    def __init__(self):
        self._code_index: Dict[str, str] = {{}}  # code -> id
        self._status_index: Dict[str, Set[str]] = {{}}  # status -> Set[id]
        self._tenant_index: Dict[str, Set[str]] = {{}}  # tenant_id -> Set[id]

    def index_entity(self, entity: {c_name}Entity):
        self._code_index[f"{{entity.tenant_id}}:{{entity.code.upper()}}"] = entity.id
        
        status_key = entity.status.upper()
        if status_key not in self._status_index:
            self._status_index[status_key] = set()
        self._status_index[status_key].add(entity.id)

        if entity.tenant_id not in self._tenant_index:
            self._tenant_index[entity.tenant_id] = set()
        self._tenant_index[entity.tenant_id].add(entity.id)

    def find_id_by_code(self, tenant_id: str, code: str) -> Optional[str]:
        return self._code_index.get(f"{{tenant_id}}:{{code.upper()}}")

    def find_ids_by_status(self, status: str) -> Set[str]:
        return self._status_index.get(status.upper(), set())
''')

    print("[PROJECTIONS & INDEXERS] Complete projections and indexers generated.")

if __name__ == '__main__':
    generate_projections_and_indexers()
