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

def generate_contracts_and_metrics():
    print("[CONTRACTS & METRICS] Generating API contracts, telemetry metrics, and SQL migration versions...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. API Contracts & Strict Validation Specifications
        write_f(f"{base_dir}/presentation/contracts.py", f'''"""
{title} — Formal API Contracts & Validation Specifications.
Defines public API response payloads, header validation, and pagination contracts for {mod}.
"""
from typing import Generic, TypeVar, List, Optional, Dict, Any
from pydantic import BaseModel, Field

T = TypeVar("T")

class {c_name}ContractRequest(BaseModel):
    """Client mutation contract payload for {title}."""
    action: str = Field(..., description="Action to perform", example="CREATE_OR_UPDATE")
    payload: Dict[str, Any] = Field(..., description="Domain entity attribute dictionary")
    client_version: str = Field(default="1.0.0", description="Client SDK version")
    idempotency_key: Optional[str] = Field(None, description="Unique UUID for idempotent retries")

class {c_name}ContractResponse(BaseModel, Generic[T]):
    """Standard unified API envelope for {title}."""
    success: bool = True
    status_code: int = 200
    message: str = "Operation executed successfully"
    data: Optional[T] = None
    errors: Optional[List[Dict[str, Any]]] = None
    telemetry: Dict[str, Any] = Field(default_factory=dict)
''')

        # 2. Prometheus / OpenTelemetry Instrumentation
        write_f(f"{base_dir}/infrastructure/metrics.py", f'''"""
{title} — Prometheus & OpenTelemetry Instrumentation.
Collects latency histograms, request counters, and error rates for {mod}.
"""
import time
import logging
from typing import Dict, Any

logger = logging.getLogger("erp.{mod}.metrics")

class {c_name}MetricsCollector:
    """Domain telemetry collector for {title}."""
    _request_count: int = 0
    _error_count: int = 0
    _total_latency_ms: float = 0.0

    @classmethod
    def record_request(cls, endpoint: str, latency_ms: float, is_error: bool = False):
        cls._request_count += 1
        cls._total_latency_ms += latency_ms
        if is_error:
            cls._error_count += 1
        logger.debug(f"Metric logged: {mod}.{{endpoint}} -> {{latency_ms:.2f}}ms (Errors: {{cls._error_count}})")

    @classmethod
    def get_stats(cls) -> Dict[str, Any]:
        avg_latency = (cls._total_latency_ms / cls._request_count) if cls._request_count > 0 else 0.0
        return {{
            "module": "{mod}",
            "total_requests": cls._request_count,
            "error_count": cls._error_count,
            "average_latency_ms": round(avg_latency, 2),
            "availability_percentage": 100.0 if cls._request_count == 0 else round((1 - cls._error_count / cls._request_count) * 100, 2)
        }}
''')

    # Extended SQL Migration Versions
    sql_migrations = [
        ("002_finance_ledger_schema.sql", """-- Detailed Finance & General Ledger Table Schema
CREATE TABLE IF NOT EXISTS erp_finance_journal_entries (
    id VARCHAR(36) PRIMARY KEY,
    tenant_id VARCHAR(64) NOT NULL,
    entry_number VARCHAR(64) UNIQUE NOT NULL,
    entry_date DATE NOT NULL,
    description TEXT NOT NULL,
    total_debit NUMERIC(15,2) NOT NULL,
    total_credit NUMERIC(15,2) NOT NULL,
    status VARCHAR(32) DEFAULT 'POSTED' NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS erp_finance_journal_lines (
    id VARCHAR(36) PRIMARY KEY,
    journal_entry_id VARCHAR(36) REFERENCES erp_finance_journal_entries(id) ON DELETE CASCADE,
    account_code VARCHAR(32) NOT NULL,
    account_name VARCHAR(255) NOT NULL,
    debit NUMERIC(15,2) DEFAULT 0.0 NOT NULL,
    credit NUMERIC(15,2) DEFAULT 0.0 NOT NULL,
    description VARCHAR(255)
);
"""),
        ("003_academic_curriculum_schema.sql", """-- Detailed Curriculum, Prerequisites & Elective Offerings
CREATE TABLE IF NOT EXISTS erp_academics_curriculum (
    id VARCHAR(36) PRIMARY KEY,
    program_id VARCHAR(64) NOT NULL,
    semester INT NOT NULL,
    course_id VARCHAR(64) NOT NULL,
    is_mandatory BOOLEAN DEFAULT TRUE NOT NULL,
    min_pass_grade VARCHAR(5) DEFAULT 'C' NOT NULL
);

CREATE TABLE IF NOT EXISTS erp_academics_prerequisites (
    id VARCHAR(36) PRIMARY KEY,
    course_id VARCHAR(64) NOT NULL,
    required_prerequisite_course_id VARCHAR(64) NOT NULL,
    min_required_grade VARCHAR(5) DEFAULT 'C' NOT NULL
);
"""),
        ("004_attendance_biometric_schema.sql", """-- Smart Biometric & Gate Attendance Logs
CREATE TABLE IF NOT EXISTS erp_attendance_sessions (
    id VARCHAR(36) PRIMARY KEY,
    tenant_id VARCHAR(64) NOT NULL,
    course_id VARCHAR(64) NOT NULL,
    faculty_id VARCHAR(64) NOT NULL,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    room_number VARCHAR(32) NOT NULL,
    total_enrolled INT NOT NULL,
    total_present INT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
"""),
        ("005_examination_transcripts_schema.sql", """-- Examinations, Moderation, Grade Points & Transcripts
CREATE TABLE IF NOT EXISTS erp_examinations_grades (
    id VARCHAR(36) PRIMARY KEY,
    student_id VARCHAR(36) NOT NULL,
    course_id VARCHAR(64) NOT NULL,
    semester INT NOT NULL,
    internal_marks NUMERIC(5,2) NOT NULL,
    end_sem_marks NUMERIC(5,2) NOT NULL,
    total_marks NUMERIC(5,2) NOT NULL,
    letter_grade VARCHAR(5) NOT NULL,
    grade_point NUMERIC(4,2) NOT NULL,
    result_status VARCHAR(20) DEFAULT 'PASS' NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);
""")
    ]

    for filename, sql in sql_migrations:
        write_f(f"database/migrations/versions/{filename}", sql.strip())

    print("[CONTRACTS & METRICS] Generated contracts, metrics, and SQL migrations.")

if __name__ == '__main__':
    generate_contracts_and_metrics()
