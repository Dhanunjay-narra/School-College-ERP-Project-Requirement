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

def generate_listeners_and_xml():
    print("[LISTENERS & XML] Generating Event Listeners and XML statutory export serializers...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. Event Listeners & WebSocket Dispatchers
        write_f(f"{base_dir}/infrastructure/event_listeners.py", f'''"""
{title} — Asynchronous Event Listeners & WebSocket Dispatchers.
"""
import logging
from typing import Dict, Any
from backend.core.events import DomainEvent, event_bus
from backend.core.websocket_manager import ws_manager

logger = logging.getLogger("erp.{mod}.listeners")

class {c_name}EventListener:
    """Subscribes to domain events in {mod} and dispatches real-time WebSocket notifications."""

    @classmethod
    async def on_entity_created(cls, event: DomainEvent):
        logger.info(f"Processing created event in {mod}: {{event.event_id}}")
        channel = f"tenant:{{event.tenant_id}}:{mod}"
        await ws_manager.broadcast(channel, {{
            "event_type": event.event_type,
            "aggregate_id": event.aggregate_id,
            "timestamp": event.occurred_at.isoformat(),
            "payload": event.payload
        }})

    @classmethod
    async def on_entity_updated(cls, event: DomainEvent):
        logger.info(f"Processing updated event in {mod}: {{event.event_id}}")
        channel = f"tenant:{{event.tenant_id}}:{mod}"
        await ws_manager.broadcast(channel, {{
            "event_type": event.event_type,
            "aggregate_id": event.aggregate_id,
            "timestamp": event.occurred_at.isoformat(),
            "payload": event.payload
        }})

    @classmethod
    def register_subscribers(cls):
        event_bus.subscribe(f"{mod}.created", cls.on_entity_created)
        event_bus.subscribe(f"{mod}.updated", cls.on_entity_updated)
''')

        # 2. Statutory XML Serializers
        write_f(f"{base_dir}/presentation/xml_serializers.py", f'''"""
{title} — Statutory XML & Regulatory Export Serializer.
Formats domain aggregate records into standard institutional XML schemas for {mod}.
"""
import xml.etree.ElementTree as ET
from typing import List
from backend.{mod}.domain.entities import {c_name}Entity

class {c_name}XMLSerializer:
    """Generates regulatory XML payloads for {title}."""

    @staticmethod
    def to_xml(entities: List[{c_name}Entity]) -> str:
        root = ET.Element("RegulatoryDataset", module="{mod}", version="1.0")
        for entity in entities:
            elem = ET.SubElement(root, "{c_name}Record", id=str(entity.id))
            ET.SubElement(elem, "TenantId").text = entity.tenant_id
            ET.SubElement(elem, "Code").text = entity.code
            ET.SubElement(elem, "Name").text = entity.name
            ET.SubElement(elem, "Status").text = entity.status
            ET.SubElement(elem, "CreatedAt").text = entity.created_at.isoformat()
        return ET.tostring(root, encoding="utf-8").decode("utf-8")
''')

    print("[LISTENERS & XML] Event listeners and XML serializers generated.")

if __name__ == '__main__':
    generate_listeners_and_xml()
