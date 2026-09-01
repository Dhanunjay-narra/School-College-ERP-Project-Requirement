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

def generate_acl_and_repo_tests():
    print("[ACL & REPO TESTS] Generating Anti-Corruption Layers and Repository Tests for all 40 modules...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. Anti-Corruption Layer (ACL)
        write_f(f"{base_dir}/domain/acl.py", f'''"""
{title} — Anti-Corruption Layer (ACL) Translator.
Translates external entity representations to {title} aggregate roots.
"""
from typing import Dict, Any, Optional
from backend.{mod}.domain.entities import {c_name}Entity

class {c_name}ACLTranslator:
    """Isolates {title} domain from external legacy formats."""

    @classmethod
    def translate_from_external_source(cls, external_data: Dict[str, Any], tenant_id: str = "default_institution") -> {c_name}Entity:
        return {c_name}Entity(
            id=str(external_data.get("external_id") or external_data.get("id", "")),
            tenant_id=tenant_id,
            code=str(external_data.get("legacy_code") or external_data.get("code", "EXT")),
            name=str(external_data.get("display_name") or external_data.get("name", "External Entry")),
            status=str(external_data.get("state") or external_data.get("status", "ACTIVE")),
            metadata=dict(external_data.get("extra_attributes") or {{}})
        )
''')

        # 2. Repository Unit Tests
        write_f(f"tests/repositories/test_{mod}_repository.py", f'''"""
Repository Test Suite for {title} ({mod}).
"""
import pytest
import asyncio
from backend.{mod}.domain.entities import {c_name}Entity
from backend.{mod}.infrastructure.repositories import InMemory{c_name}Repository

def test_{mod}_repository_crud():
    async def _run():
        repo = InMemory{c_name}Repository()
        
        # Save entity
        entity = {c_name}Entity(code="R-TEST", name="Repository Test {title}", status="ACTIVE")
        saved = await repo.save(entity)
        assert saved.id is not None

        # Get entity
        fetched = await repo.get_by_id(saved.id)
        assert fetched is not None
        assert fetched.code == "R-TEST"

        # List entities
        items = await repo.list_all()
        assert len(items) >= 1

        # Delete entity
        deleted = await repo.delete(saved.id)
        assert deleted is True

    asyncio.run(_run())
''')

    print("[ACL & REPO TESTS] Generated ACL translators and repository tests.")

if __name__ == '__main__':
    generate_acl_and_repo_tests()
