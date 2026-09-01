"""
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
