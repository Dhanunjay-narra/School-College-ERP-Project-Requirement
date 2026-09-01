"""
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
