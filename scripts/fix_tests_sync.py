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

def generate_sync_tests():
    print("[TESTS] Generating synchronous-wrapped tests for 100% test compatibility...")

    for mod, title in MODULES:
        if mod in ["identity", "organization", "students"]:
            continue
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        write_f(f"tests/unit/test_{mod}.py", f'''"""
Unit Test Suite for {title} ({mod}).
"""
import pytest
import asyncio
from datetime import datetime
from backend.{mod}.domain.entities import {c_name}Entity
from backend.{mod}.application.commands import Create{c_name}Command, Update{c_name}Command, Delete{c_name}Command
from backend.{mod}.application.handlers import {c_name}CommandHandler
from backend.{mod}.infrastructure.repositories import InMemory{c_name}Repository
from backend.{mod}.presentation.serializers import {c_name}Serializer

def test_{mod}_entity_creation():
    entity = {c_name}Entity(code="TEST-01", name="Test {c_name} Item", status="ACTIVE")
    assert entity.code == "TEST-01"
    assert entity.status == "ACTIVE"
    entity.update_status("INACTIVE")
    assert entity.status == "INACTIVE"
    assert "code" in entity.to_dict()

def test_{mod}_command_handler_flow():
    async def _run_flow():
        repo = InMemory{c_name}Repository()
        handler = {c_name}CommandHandler(repo)

        create_cmd = Create{c_name}Command(code="TEST-02", name="Automated {c_name}")
        created = await handler.handle_create(create_cmd)
        assert created.id is not None
        assert created.code == "TEST-02"

        update_cmd = Update{c_name}Command(id=created.id, name="Updated {c_name}")
        updated = await handler.handle_update(update_cmd)
        assert updated.name == "Updated {c_name}"

        item = await repo.get_by_id(created.id)
        assert item is not None

        deleted = await handler.handle_delete(Delete{c_name}Command(id=created.id))
        assert deleted is True

    asyncio.run(_run_flow())

def test_{mod}_serializer():
    entity = {c_name}Entity(id="SERIAL-01", code="S01", name="Serialization Item", status="ACTIVE")
    json_str = {c_name}Serializer.to_json(entity)
    assert "SERIAL-01" in json_str
    csv_str = {c_name}Serializer.to_csv([entity])
    assert "SERIAL-01" in csv_str
''')

    write_f("tests/unit/test_identity.py", '''"""
Unit Tests for Identity Domain.
"""
import pytest
import asyncio
from backend.identity.domain.entities import User, Role
from backend.identity.domain.value_objects import RoleType
from backend.identity.infrastructure.repositories import default_user_repo, default_role_repo
from backend.identity.application.services import AuthenticationService

def test_user_entity():
    user = User(
        id="U-1", email="test@erp.edu", hashed_password="pw",
        first_name="John", last_name="Doe", roles=[Role(id="R-1", name="STUDENT", role_type=RoleType.STUDENT)]
    )
    assert user.full_name == "John Doe"
    assert user.has_role(RoleType.STUDENT)
    assert not user.is_locked()

def test_auth_service_authenticate():
    async def _run():
        svc = AuthenticationService(default_user_repo, default_role_repo)
        result = await svc.authenticate("superadmin@erp.edu", "Password@123")
        assert result["user"]["email"] == "superadmin@erp.edu"
    asyncio.run(_run())
''')

    write_f("tests/unit/test_organization.py", '''"""
Unit Tests for Organization Domain.
"""
import pytest
import asyncio
from backend.organization.domain.entities import Institution, Campus, Department
from backend.organization.domain.value_objects import InstitutionType, DepartmentType
from backend.organization.infrastructure.repositories import default_org_repo

def test_institution_entity():
    inst = Institution(id="I-1", name="Apex University", code="AU", institution_type=InstitutionType.UNIVERSITY)
    assert inst.code == "AU"
    assert inst.institution_type == InstitutionType.UNIVERSITY

def test_org_repo_get_institution():
    async def _run():
        inst = await default_org_repo.get_institution("default_institution")
        assert inst is not None
        assert inst.code == "AITM"
    asyncio.run(_run())
''')

    write_f("tests/unit/test_students.py", '''"""
Unit Tests for Student Domain.
"""
import pytest
from datetime import date
from backend.students.domain.entities import Student
from backend.students.domain.value_objects import StudentStatus, Gender, BloodGroup

def test_student_entity():
    student = Student(
        id="S-1", user_id="U-1", admission_number="A1", roll_number="R1",
        first_name="Aarav", last_name="Patel", date_of_birth=date(2004,1,1),
        gender=Gender.MALE, email="a@erp.edu", phone_number="123",
        department_id="CS", program_id="BTECH"
    )
    assert student.full_name == "Aarav Patel"
    assert student.status == StudentStatus.ACTIVE
    student.transition_status(StudentStatus.GRADUATED)
    assert student.status == StudentStatus.GRADUATED
''')

    write_f("tests/integration/test_student_admission_workflow.py", '''"""
Integration Test: End-to-End Student Lifecycle Workflow.
"""
import pytest
from datetime import date
from backend.students.domain.entities import Student
from backend.students.domain.value_objects import StudentStatus, Gender, BloodGroup

def test_admission_to_enrollment_workflow():
    student = Student(
        id="STU-INT-001",
        user_id="USR-INT-001",
        admission_number="ADM-INT-2026",
        roll_number="26INT001",
        first_name="Rohan",
        last_name="Gupta",
        date_of_birth=date(2005, 3, 10),
        gender=Gender.MALE,
        email="rohan.gupta@erp.edu",
        phone_number="+91-9988776655",
        department_id="CS-DEP",
        program_id="BTECH-CSE",
        current_semester=1,
        status=StudentStatus.ADMITTED
    )
    assert student.status == StudentStatus.ADMITTED
    student.transition_status(StudentStatus.ACTIVE)
    assert student.status == StudentStatus.ACTIVE
''')

if __name__ == '__main__':
    generate_sync_tests()
