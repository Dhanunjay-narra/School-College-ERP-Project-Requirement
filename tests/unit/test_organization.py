"""
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
