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

def generate_depth():
    print("[DEPTH] Generating domain business rules, GraphQL types, and database table models...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. Domain Business Services & State Transition Rules
        write_f(f"{base_dir}/domain/services.py", f'''"""
{title} — Domain Business Rules & Invariant Validation Service.
"""
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from backend.{mod}.domain.entities import {c_name}Entity
from backend.core.exceptions import DomainException, ValidationException

logger = logging.getLogger("erp.{mod}.domain_service")

class {c_name}DomainService:
    """Encapsulates pure business logic and invariant checks for {title}."""

    @staticmethod
    def validate_code_format(code: str) -> bool:
        """Validate standard uppercase alphanumeric format with hyphens."""
        if not code or len(code) < 2 or len(code) > 64:
            raise ValidationException("Code must be between 2 and 64 characters in length.")
        if not code.replace("-", "").isalnum():
            raise ValidationException("Code must contain only alphanumeric characters and hyphens.")
        return True

    @staticmethod
    def assert_valid_state_transition(current_status: str, new_status: str):
        """State machine invariant validation for {mod}."""
        valid_transitions = {{
            "DRAFT": ["PENDING_REVIEW", "ACTIVE", "ARCHIVED"],
            "PENDING_REVIEW": ["APPROVED", "REJECTED", "ACTIVE"],
            "APPROVED": ["ACTIVE", "SUSPENDED", "COMPLETED"],
            "ACTIVE": ["SUSPENDED", "INACTIVE", "ARCHIVED", "COMPLETED"],
            "SUSPENDED": ["ACTIVE", "TERMINATED", "ARCHIVED"],
            "INACTIVE": ["ACTIVE", "ARCHIVED"],
            "COMPLETED": ["ARCHIVED"],
            "ARCHIVED": []
        }}
        allowed = valid_transitions.get(current_status.upper(), ["ACTIVE", "INACTIVE", "ARCHIVED"])
        if new_status.upper() not in allowed and current_status.upper() != new_status.upper():
            raise DomainException(f"Invalid state transition from '{{current_status}}' to '{{new_status}}'.")

    @staticmethod
    def calculate_operational_health_score(entity: {c_name}Entity) -> float:
        """Calculate dynamic health and operational readiness score (0.0 - 100.0)."""
        score = 100.0
        if entity.status == "SUSPENDED":
            score -= 40.0
        elif entity.status == "INACTIVE":
            score -= 60.0
        elif entity.status == "ARCHIVED":
            score -= 90.0
        return max(0.0, score)
''')

        # 2. GraphQL Schema & Federation Resolvers
        write_f(f"{base_dir}/presentation/graphql_types.py", f'''"""
{title} — GraphQL Type Definitions & Resolvers.
Provides federated GraphQL schema mappings for {mod}.
"""
from typing import Optional, List, Dict, Any

class {c_name}GraphQLType:
    """GraphQL Object Type for {c_name}."""
    def __init__(self, id: str, code: str, name: str, status: str, tenant_id: str):
        self.id = id
        self.code = code
        self.name = name
        self.status = status
        self.tenant_id = tenant_id

    @classmethod
    def from_entity(cls, entity) -> "{c_name}GraphQLType":
        return cls(
            id=entity.id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            tenant_id=entity.tenant_id
        )

    def resolve_display_label(self) -> str:
        return f"[{{self.code}}] {{self.name}} ({{self.status}})"
''')

    print("[DEPTH] Domain business rules and GraphQL types generated.")

if __name__ == '__main__':
    generate_depth()
