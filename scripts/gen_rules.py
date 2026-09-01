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

def generate_rules_and_migrations():
    print("[RULES & MIGRATIONS] Generating business rules, documentation specs, and SQL migration files...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. Domain Business Rules & Constraint Solvers
        write_f(f"{base_dir}/domain/rules.py", f'''"""
{title} — Business Policy Rules & Constraints.
Defines domain policy specifications, operational invariants, and eligibility predicates for {mod}.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime
from backend.core.exceptions import DomainException, ValidationException

class {c_name}BusinessRules:
    """Domain rule evaluator for {title}."""

    @classmethod
    def evaluate_creation_policy(cls, data: Dict[str, Any], tenant_id: str) -> bool:
        """Validate institutional policy requirements prior to creation."""
        if not data.get("code"):
            raise ValidationException("Unique identifier code is strictly required by institutional policy.")
        if len(str(data.get("name", ""))) < 3:
            raise ValidationException("Entity name must contain at least 3 characters.")
        return True

    @classmethod
    def evaluate_modification_policy(cls, entity_id: str, updates: Dict[str, Any], user_roles: List[str]) -> bool:
        """Enforce permission rules for entity modifications."""
        privileged_roles = ["SUPER_ADMIN", "INSTITUTION_ADMIN", "PRINCIPAL", "HOD"]
        if not any(r in privileged_roles for r in user_roles):
            # Check standard domain updates
            if "status" in updates and updates["status"] in ["DELETED", "PURGED", "ARCHIVED"]:
                raise DomainException("Only authorized administrators can purge or archive operational records.")
        return True

    @classmethod
    def compute_risk_score(cls, entity_state: Dict[str, Any]) -> float:
        """Compute operational risk score (0.0 to 10.0) based on domain invariants."""
        risk = 1.0
        if entity_state.get("status") == "SUSPENDED":
            risk += 4.5
        elif entity_state.get("status") == "PENDING_REVIEW":
            risk += 2.0
        return min(10.0, risk)
''')

        # 2. API Documentation Specifications & Mock Data Generators
        write_f(f"{base_dir}/presentation/documentation.py", f'''"""
{title} — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class {c_name}DocSpec:
    """OpenAPI documentation and reference fixtures for {title}."""

    SUMMARY = "{title} API endpoint group for academic and institutional operations."
    TAGS = ["{title}"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {{
            "action": "CREATE_RECORD",
            "payload": {{
                "code": "{mod.upper()[:4]}-2026-001",
                "name": "Standard {title} Operational Record",
                "status": "ACTIVE",
                "department": "Computer Science & Engineering",
                "campus": "Main Academic Campus"
            }},
            "client_version": "1.0.0"
        }}

    @staticmethod
    def get_sample_response_fixture() -> Dict[str, Any]:
        return {{
            "success": True,
            "status_code": 200,
            "message": "Resource processed successfully",
            "data": {{
                "id": "{mod.upper()[:4]}-UUID-8842",
                "tenant_id": "default_institution",
                "code": "{mod.upper()[:4]}-2026-001",
                "name": "Standard {title} Operational Record",
                "status": "ACTIVE"
            }}
        }}
''')

    # Comprehensive SQL Migrations for all remaining domains
    extended_migrations = [
        ("006_procurement_po_grn.sql", """-- Procurement, Purchase Orders & Goods Receipt Notes
CREATE TABLE IF NOT EXISTS erp_procurement_orders (
    id VARCHAR(36) PRIMARY KEY,
    po_number VARCHAR(64) UNIQUE NOT NULL,
    vendor_id VARCHAR(36) NOT NULL,
    total_amount NUMERIC(15,2) NOT NULL,
    status VARCHAR(32) DEFAULT 'DRAFT' NOT NULL,
    delivery_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS erp_procurement_grn (
    id VARCHAR(36) PRIMARY KEY,
    grn_number VARCHAR(64) UNIQUE NOT NULL,
    po_id VARCHAR(36) REFERENCES erp_procurement_orders(id),
    received_by VARCHAR(36) NOT NULL,
    inspection_passed BOOLEAN DEFAULT TRUE NOT NULL,
    received_date DATE NOT NULL
);
"""),
        ("007_inventory_warehouses_skus.sql", """-- Multi-Store Warehouses and Item SKUs
CREATE TABLE IF NOT EXISTS erp_inventory_warehouses (
    id VARCHAR(36) PRIMARY KEY,
    code VARCHAR(32) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    campus_id VARCHAR(36) NOT NULL,
    manager_id VARCHAR(36)
);

CREATE TABLE IF NOT EXISTS erp_inventory_items (
    id VARCHAR(36) PRIMARY KEY,
    sku VARCHAR(64) UNIQUE NOT NULL,
    item_name VARCHAR(255) NOT NULL,
    warehouse_id VARCHAR(36) REFERENCES erp_inventory_warehouses(id),
    quantity_on_hand INT DEFAULT 0 NOT NULL,
    reorder_level INT DEFAULT 10 NOT NULL,
    unit_of_measure VARCHAR(32) DEFAULT 'Units' NOT NULL
);
"""),
        ("008_assets_depreciation_maintenance.sql", """-- Asset Lifecycle, QR Tagging, and Maintenance Tickets
CREATE TABLE IF NOT EXISTS erp_assets_registry (
    id VARCHAR(36) PRIMARY KEY,
    asset_tag VARCHAR(64) UNIQUE NOT NULL,
    asset_name VARCHAR(255) NOT NULL,
    category VARCHAR(64) NOT NULL,
    purchase_cost NUMERIC(12,2) NOT NULL,
    current_book_value NUMERIC(12,2) NOT NULL,
    depreciation_rate_annual NUMERIC(5,2) DEFAULT 10.0 NOT NULL,
    location_room_id VARCHAR(36) NOT NULL,
    assigned_user_id VARCHAR(36)
);
"""),
        ("009_transport_fleet_gps.sql", """-- Transportation Fleet, Routes, and Real-Time Telemetry
CREATE TABLE IF NOT EXISTS erp_transport_fleet (
    id VARCHAR(36) PRIMARY KEY,
    vehicle_number VARCHAR(32) UNIQUE NOT NULL,
    vehicle_type VARCHAR(32) DEFAULT 'BUS' NOT NULL,
    seating_capacity INT NOT NULL,
    driver_user_id VARCHAR(36) NOT NULL,
    insurance_valid_until DATE NOT NULL,
    fitness_valid_until DATE NOT NULL
);
"""),
        ("010_hostel_housing_mess.sql", """-- Hostel Residential Life, Rooms, and Mess Services
CREATE TABLE IF NOT EXISTS erp_hostels_buildings (
    id VARCHAR(36) PRIMARY KEY,
    building_name VARCHAR(255) NOT NULL,
    gender_type VARCHAR(20) NOT NULL,
    total_rooms INT NOT NULL,
    warden_user_id VARCHAR(36) NOT NULL
);
"""),
        ("011_library_circulation_rfid.sql", """-- Library Catalog, MARC21, and RFID Circulation
CREATE TABLE IF NOT EXISTS erp_library_catalog (
    id VARCHAR(36) PRIMARY KEY,
    isbn VARCHAR(32) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    authors VARCHAR(255) NOT NULL,
    total_copies INT DEFAULT 1 NOT NULL,
    available_copies INT DEFAULT 1 NOT NULL,
    shelf_location VARCHAR(64) NOT NULL
);
"""),
        ("012_hr_recruitment_ats.sql", """-- HR Employee Profiles, Contracts, and Recruitment ATS
CREATE TABLE IF NOT EXISTS erp_hr_employees (
    id VARCHAR(36) PRIMARY KEY,
    employee_code VARCHAR(32) UNIQUE NOT NULL,
    user_id VARCHAR(36) NOT NULL,
    designation VARCHAR(100) NOT NULL,
    department_id VARCHAR(36) NOT NULL,
    joining_date DATE NOT NULL,
    basic_monthly_salary NUMERIC(12,2) NOT NULL,
    status VARCHAR(32) DEFAULT 'ACTIVE' NOT NULL
);
"""),
        ("013_payroll_structures_payslips.sql", """-- Payroll Processing, Salary Structures, and Payslips
CREATE TABLE IF NOT EXISTS erp_payroll_disbursements (
    id VARCHAR(36) PRIMARY KEY,
    employee_id VARCHAR(36) NOT NULL,
    month_year VARCHAR(20) NOT NULL,
    basic_pay NUMERIC(12,2) NOT NULL,
    allowances NUMERIC(12,2) NOT NULL,
    deductions NUMERIC(12,2) NOT NULL,
    net_salary NUMERIC(12,2) NOT NULL,
    disbursement_status VARCHAR(32) DEFAULT 'DISBURSED' NOT NULL
);
"""),
        ("014_crm_alumni_donations.sql", """-- Institutional CRM, Alumni Network, and Endowments
CREATE TABLE IF NOT EXISTS erp_alumni_records (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    graduation_year INT NOT NULL,
    current_company VARCHAR(255),
    designation VARCHAR(100),
    total_donations_contributed NUMERIC(12,2) DEFAULT 0.0
);
"""),
        ("015_workflows_approval_chains.sql", """-- Configurable Workflows and Multi-Tier Approvals
CREATE TABLE IF NOT EXISTS erp_workflow_instances (
    id VARCHAR(36) PRIMARY KEY,
    workflow_definition_name VARCHAR(100) NOT NULL,
    initiator_user_id VARCHAR(36) NOT NULL,
    current_tier_number INT DEFAULT 1 NOT NULL,
    approval_status VARCHAR(32) DEFAULT 'PENDING' NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
""")
    ]

    for filename, sql in extended_migrations:
        write_f(f"database/migrations/versions/{filename}", sql.strip())

    print("[RULES & MIGRATIONS] Rules, documentation specs, and SQL migrations generated.")

if __name__ == '__main__':
    generate_rules_and_migrations()
