import os
from pathlib import Path
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

def generate_expanded_cqrs():
    print("[CQRS] Generating CQRS commands, queries, event handlers, and serializers for all 40 modules...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. Application Commands
        write_f(f"{base_dir}/application/commands.py", f'''"""
{title} — CQRS Commands.
Defines immutable command structures and validations for {mod}.
"""
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List
from datetime import datetime
import uuid

@dataclass(frozen=True)
class Create{c_name}Command:
    code: str
    name: str
    tenant_id: str = "default_institution"
    status: str = "ACTIVE"
    metadata: Dict[str, Any] = field(default_factory=dict)
    command_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass(frozen=True)
class Update{c_name}Command:
    id: str
    name: Optional[str] = None
    status: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    tenant_id: str = "default_institution"
    command_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass(frozen=True)
class Delete{c_name}Command:
    id: str
    tenant_id: str = "default_institution"
    reason: str = "Administrative action"
    command_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass(frozen=True)
class BatchProcess{c_name}Command:
    item_ids: List[str]
    action: str
    tenant_id: str = "default_institution"
    parameters: Dict[str, Any] = field(default_factory=dict)
    command_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)
''')

        # 2. Application Queries
        write_f(f"{base_dir}/application/queries.py", f'''"""
{title} — CQRS Queries.
Defines read-model queries, filtering criteria, and sorting specifications for {mod}.
"""
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

@dataclass(frozen=True)
class Get{c_name}ByIdQuery:
    id: str
    tenant_id: str = "default_institution"
    include_metadata: bool = True

@dataclass(frozen=True)
class List{c_name}sQuery:
    tenant_id: str = "default_institution"
    status_filter: Optional[str] = None
    search_term: Optional[str] = None
    page: int = 1
    page_size: int = 20
    sort_by: str = "created_at"
    sort_desc: bool = True

@dataclass(frozen=True)
class Count{c_name}sQuery:
    tenant_id: str = "default_institution"
    status_filter: Optional[str] = None

@dataclass(frozen=True)
class Search{c_name}sQuery:
    query: str
    tenant_id: str = "default_institution"
    facets: Optional[Dict[str, Any]] = None
    limit: int = 50
''')

        # 3. Application Event & Command Handlers
        write_f(f"{base_dir}/application/handlers.py", f'''"""
{title} — CQRS Command and Event Handlers.
Implements asynchronous dispatch and domain logic coordination for {mod}.
"""
import logging
from typing import Optional, Dict, Any, List
from backend.{mod}.domain.entities import {c_name}Entity
from backend.{mod}.domain.repositories import I{c_name}Repository
from backend.{mod}.domain.events import {c_name}CreatedEvent, {c_name}UpdatedEvent
from backend.{mod}.application.commands import Create{c_name}Command, Update{c_name}Command, Delete{c_name}Command
from backend.core.events import DomainEvent, event_bus
from backend.core.exceptions import EntityNotFoundException, ValidationException

logger = logging.getLogger("erp.{mod}.handlers")

class {c_name}CommandHandler:
    def __init__(self, repository: I{c_name}Repository):
        self.repository = repository

    async def handle_create(self, cmd: Create{c_name}Command) -> {c_name}Entity:
        logger.info(f"Handling Create{c_name}Command: {{cmd.code}}")
        entity = {c_name}Entity(
            code=cmd.code,
            name=cmd.name,
            status=cmd.status,
            tenant_id=cmd.tenant_id,
            metadata=cmd.metadata
        )
        saved = await self.repository.save(entity)
        await event_bus.publish({c_name}CreatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_update(self, cmd: Update{c_name}Command) -> {c_name}Entity:
        logger.info(f"Handling Update{c_name}Command for ID: {{cmd.id}}")
        entity = await self.repository.get_by_id(cmd.id, cmd.tenant_id)
        if not entity:
            raise EntityNotFoundException("{c_name}", cmd.id)
        
        if cmd.name:
            entity.name = cmd.name
        if cmd.status:
            entity.update_status(cmd.status)
        if cmd.metadata:
            for k, v in cmd.metadata.items():
                entity.update_metadata(k, v)

        saved = await self.repository.save(entity)
        await event_bus.publish({c_name}UpdatedEvent(saved.id, cmd.tenant_id, saved.to_dict()))
        return saved

    async def handle_delete(self, cmd: Delete{c_name}Command) -> bool:
        logger.info(f"Handling Delete{c_name}Command for ID: {{cmd.id}} (Reason: {{cmd.reason}})")
        return await self.repository.delete(cmd.id, cmd.tenant_id)

async def handle_domain_event(event: DomainEvent):
    """Generic async domain event handler for {mod}."""
    logger.info(f"Received domain event in {mod}: {{event.event_type}} (Aggregate: {{event.aggregate_id}})")
''')

        # 4. Presentation Serializers & Exporters
        write_f(f"{base_dir}/presentation/serializers.py", f'''"""
{title} — Serializers, Formatter & Exporters.
Provides CSV, JSON, and XML serialization routines for {mod}.
"""
import json
import csv
import io
from typing import List, Dict, Any
from backend.{mod}.domain.entities import {c_name}Entity

class {c_name}Serializer:
    @staticmethod
    def to_json(entity: {c_name}Entity) -> str:
        return json.dumps(entity.to_dict(), indent=2)

    @staticmethod
    def to_csv(entities: List[{c_name}Entity]) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["ID", "Tenant ID", "Code", "Name", "Status", "Created At"])
        for e in entities:
            writer.writerow([e.id, e.tenant_id, e.code, e.name, e.status, e.created_at.isoformat()])
        return output.getvalue()

    @staticmethod
    def to_summary(entity: {c_name}Entity) -> Dict[str, Any]:
        return {{
            "id": entity.id,
            "title": f"{{entity.code}} — {{entity.name}}",
            "status": entity.status,
            "created_at": entity.created_at.strftime("%Y-%m-%d %H:%M")
        }}
''')

    print("[CQRS] Complete CQRS layers generated for all 40 modules.")

if __name__ == '__main__':
    generate_expanded_cqrs()
