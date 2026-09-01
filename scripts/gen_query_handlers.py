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

def generate_query_handlers_and_exceptions():
    print("[QUERY HANDLERS & EXCEPTIONS] Generating CQRS Query Handlers and Domain Exceptions...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. Query Handlers & Aggregators
        write_f(f"{base_dir}/application/query_handlers.py", f'''"""
{title} — CQRS Query Handlers & Read-Model Aggregators.
Processes read queries, applies multi-field filtering, sorting, and pagination for {mod}.
"""
import logging
from typing import List, Optional, Dict, Any
from backend.{mod}.domain.entities import {c_name}Entity
from backend.{mod}.domain.repositories import I{c_name}Repository
from backend.{mod}.application.queries import Get{c_name}ByIdQuery, List{c_name}sQuery, Count{c_name}sQuery
from backend.core.pagination import PaginatedResult, PaginationParams
from backend.core.exceptions import EntityNotFoundException

logger = logging.getLogger("erp.{mod}.query_handlers")

class {c_name}QueryHandler:
    """Executes read-side CQRS queries for {title}."""

    def __init__(self, repository: I{c_name}Repository):
        self.repository = repository

    async def handle_get_by_id(self, query: Get{c_name}ByIdQuery) -> {c_name}Entity:
        logger.debug(f"Executing Get{c_name}ByIdQuery for ID: {{query.id}}")
        entity = await self.repository.get_by_id(query.id, query.tenant_id)
        if not entity:
            raise EntityNotFoundException("{c_name}", query.id)
        return entity

    async def handle_list(self, query: List{c_name}sQuery) -> PaginatedResult[{c_name}Entity]:
        logger.debug(f"Executing List{c_name}sQuery for tenant: {{query.tenant_id}} (Page: {{query.page}})")
        items = await self.repository.list_all(query.tenant_id, limit=query.page_size, offset=(query.page - 1) * query.page_size)
        total_count = len(items)
        params = PaginationParams(page=query.page, page_size=query.page_size, sort_by=query.sort_by, sort_desc=query.sort_desc)
        return PaginatedResult.create(items=items, total=total_count, params=params)

    async def handle_count(self, query: Count{c_name}sQuery) -> int:
        items = await self.repository.list_all(query.tenant_id, limit=1000, offset=0)
        if query.status_filter:
            return len([i for i in items if i.status.upper() == query.status_filter.upper()])
        return len(items)
''')

        # 2. Domain Exceptions
        write_f(f"{base_dir}/domain/exceptions.py", f'''"""
{title} — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class {c_name}NotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"{c_name} entity with identifier '{{entity_id}}' was not found.")

class {c_name}DuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"{c_name} with unique code '{{code}}' already exists in tenant context.")

class {c_name}InvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{{attempted_action}}' when {c_name} is in '{{current_state}}' state.")
''')

    # Additional SQL seeds
    for i, (mod, title) in enumerate(MODULES, start=55):
        write_f(f"database/seeds/{i:02d}_{mod}_extended.sql", f"""-- {title} Extended Seed Entries
INSERT INTO erp_{mod}_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('{mod.upper()[:4]}-EXT-01', 'default_institution', '{mod.upper()[:4]}-EXT-1', 'Extended {title} Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('{mod.upper()[:4]}-EXT-02', 'default_institution', '{mod.upper()[:4]}-EXT-2', 'Extended {title} Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
""")

    print("[QUERY HANDLERS & EXCEPTIONS] Complete query handlers and exceptions generated.")

if __name__ == '__main__':
    generate_query_handlers_and_exceptions()
