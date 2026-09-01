from writer_util import write_f

write_f("tests/unit/test_identity.py", '''"""
Unit Tests for Identity Domain.
"""
import pytest
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

@pytest.mark.asyncio
async def test_auth_service_authenticate():
    svc = AuthenticationService(default_user_repo, default_role_repo)
    result = await svc.authenticate("superadmin@erp.edu", "Password@123")
    assert result["user"]["email"] == "superadmin@erp.edu"
''')

write_f("tests/unit/test_organization.py", '''"""
Unit Tests for Organization Domain.
"""
import pytest
from backend.organization.domain.entities import Institution, Campus, Department
from backend.organization.domain.value_objects import InstitutionType, DepartmentType
from backend.organization.infrastructure.repositories import default_org_repo

def test_institution_entity():
    inst = Institution(id="I-1", name="Apex University", code="AU", institution_type=InstitutionType.UNIVERSITY)
    assert inst.code == "AU"
    assert inst.institution_type == InstitutionType.UNIVERSITY

@pytest.mark.asyncio
async def test_org_repo_get_institution():
    inst = await default_org_repo.get_institution("default_institution")
    assert inst is not None
    assert inst.code == "AITM"
''')

write_f("tests/unit/test_students.py", '''"""
Unit Tests for Student Domain.
"""
import pytest
from datetime import date
from backend.students.domain.entities import Student
from backend.students.domain.value_objects import StudentStatus, Gender, BloodGroup
from backend.students.infrastructure.repositories import default_student_repo

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

write_f("pytest.ini", '''[pytest]
asyncio_mode = auto
filterwarnings =
    ignore::DeprecationWarning
    ignore::UserWarning
    ignore::pytest.PytestUnknownMarkWarning
''')
