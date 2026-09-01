from writer_util import write_f

write_f("tests/repositories/test_identity_repository.py", '''"""
Repository Test Suite for Identity.
"""
import pytest
import asyncio
from backend.identity.domain.entities import User, Role
from backend.identity.domain.value_objects import RoleType
from backend.identity.infrastructure.repositories import default_user_repo

def test_identity_repository_crud():
    async def _run():
        user = await default_user_repo.get_by_email("superadmin@erp.edu", "default_institution")
        assert user is not None
        assert user.has_role(RoleType.SUPER_ADMIN)
    asyncio.run(_run())
''')

write_f("tests/repositories/test_organization_repository.py", '''"""
Repository Test Suite for Organization.
"""
import pytest
import asyncio
from backend.organization.infrastructure.repositories import default_org_repo

def test_organization_repository_crud():
    async def _run():
        inst = await default_org_repo.get_institution("default_institution")
        assert inst is not None
        assert inst.code == "AITM"
    asyncio.run(_run())
''')

write_f("tests/repositories/test_students_repository.py", '''"""
Repository Test Suite for Students.
"""
import pytest
import asyncio
from backend.students.infrastructure.repositories import default_student_repo

def test_students_repository_crud():
    async def _run():
        student = await default_student_repo.get_by_id("STU-2026-001")
        assert student is not None
        assert student.roll_number == "24CSE042"
    asyncio.run(_run())
''')
