"""
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
