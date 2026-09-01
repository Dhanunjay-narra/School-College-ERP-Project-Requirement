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

def generate_mappers_and_fixtures():
    print("[MAPPERS & FIXTURES] Generating Domain Data Mappers and Pytest Fixtures for all 40 modules...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. Domain Data Mappers
        write_f(f"{base_dir}/infrastructure/mappers.py", f'''"""
{title} — Domain Data Mapper & Entity Hydration.
Converts between SQLAlchemy ORM models, Pydantic DTOs, and pure DDD Aggregate Roots for {mod}.
"""
from typing import Dict, Any, Optional
from datetime import datetime
from backend.{mod}.domain.entities import {c_name}Entity
from backend.{mod}.presentation.schemas import {c_name}Response

class {c_name}DataMapper:
    """Bidirectional persistence mapper for {title}."""

    @staticmethod
    def to_domain(raw_dict: Dict[str, Any]) -> {c_name}Entity:
        return {c_name}Entity(
            id=raw_dict.get("id"),
            tenant_id=raw_dict.get("tenant_id", "default_institution"),
            code=raw_dict.get("code", "DEFAULT"),
            name=raw_dict.get("name", "Default {title}"),
            status=raw_dict.get("status", "ACTIVE"),
            metadata=raw_dict.get("metadata", {{}})
        )

    @staticmethod
    def to_persistence(entity: {c_name}Entity) -> Dict[str, Any]:
        return {{
            "id": entity.id,
            "tenant_id": entity.tenant_id,
            "code": entity.code,
            "name": entity.name,
            "status": entity.status,
            "details_json": entity.metadata,
            "updated_at": datetime.utcnow()
        }}

    @staticmethod
    def to_response_dto(entity: {c_name}Entity) -> {c_name}Response:
        return {c_name}Response(
            id=entity.id,
            tenant_id=entity.tenant_id,
            code=entity.code,
            name=entity.name,
            status=entity.status,
            metadata=entity.metadata,
            created_at=entity.created_at.isoformat(),
            updated_at=entity.updated_at.isoformat()
        )
''')

        # 2. Pytest Fixture Files
        write_f(f"tests/fixtures/fixture_{mod}.py", f'''"""
Pytest Fixtures for {title} ({mod}).
"""
import pytest
from backend.{mod}.domain.entities import {c_name}Entity

@pytest.fixture
def sample_{mod}_entity() -> {c_name}Entity:
    return {c_name}Entity(
        id="{mod.upper()[:4]}-TEST-01",
        code="{mod.upper()[:4]}-SAMPLE",
        name="Sample {title} Entity for Pytest Verification",
        status="ACTIVE"
    )
''')

    print("[MAPPERS & FIXTURES] Complete mappers and fixtures generated.")

if __name__ == '__main__':
    generate_mappers_and_fixtures()
