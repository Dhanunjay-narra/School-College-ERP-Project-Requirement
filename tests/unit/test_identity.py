"""
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
