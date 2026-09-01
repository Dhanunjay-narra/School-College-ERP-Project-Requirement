"""
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
