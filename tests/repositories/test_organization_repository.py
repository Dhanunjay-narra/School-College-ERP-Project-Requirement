"""
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
