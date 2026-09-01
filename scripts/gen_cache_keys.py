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

def generate_cache_keys():
    print("[CACHE KEYS] Generating Redis Cache Key Generators for all 40 modules...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        write_f(f"{base_dir}/infrastructure/cache_keys.py", f'''"""
{title} — Redis Cache Key Formatters & Invalidation Policies.
"""
from typing import Optional

class {c_name}CacheKeys:
    """Standardized Redis key generator for {title}."""

    PREFIX = "erp:{mod}"

    @classmethod
    def entity_key(cls, entity_id: str, tenant_id: str = "default_institution") -> str:
        return f"{{cls.PREFIX}}:{{tenant_id}}:entity:{{entity_id}}"

    @classmethod
    def list_pattern(cls, tenant_id: str = "default_institution") -> str:
        return f"{{cls.PREFIX}}:{{tenant_id}}:list:*"

    @classmethod
    def summary_key(cls, tenant_id: str = "default_institution") -> str:
        return f"{{cls.PREFIX}}:{{tenant_id}}:summary"
''')

    print("[CACHE KEYS] Generated cache keys.")

if __name__ == '__main__':
    generate_cache_keys()
