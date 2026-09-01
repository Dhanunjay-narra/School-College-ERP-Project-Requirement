"""
Student Repositories.
"""
from typing import List, Optional, Dict
from datetime import date
from backend.students.domain.entities import Student
from backend.students.domain.value_objects import StudentStatus, Gender, BloodGroup

class InMemoryStudentRepository:
    def __init__(self):
        self._students: Dict[str, Student] = {}
        self._seed_data()

    def _seed_data(self):
        demo_student = Student(
            id="STU-2026-001",
            user_id="USR-STUDENT-001",
            admission_number="ADM-2024-CSE-042",
            roll_number="24CSE042",
            first_name="Aarav",
            last_name="Patel",
            date_of_birth=date(2004, 5, 14),
            gender=Gender.MALE,
            email="student.aarav@erp.edu",
            phone_number="+91-9876543210",
            department_id="CS-DEP",
            program_id="BTECH-CSE",
            current_semester=4,
            section="A",
            status=StudentStatus.ACTIVE,
            blood_group=BloodGroup.O_POSITIVE,
            cgpa=8.85,
            attendance_percentage=94.2
        )
        self._students[demo_student.id] = demo_student

        # Seed more students
        stu2 = Student(
            id="STU-2026-002",
            user_id="USR-STUDENT-002",
            admission_number="ADM-2024-CSE-043",
            roll_number="24CSE043",
            first_name="Diya",
            last_name="Rao",
            date_of_birth=date(2004, 8, 22),
            gender=Gender.FEMALE,
            email="diya.rao@erp.edu",
            phone_number="+91-9876543211",
            department_id="CS-DEP",
            program_id="BTECH-CSE",
            current_semester=4,
            section="A",
            status=StudentStatus.ACTIVE,
            blood_group=BloodGroup.A_POSITIVE,
            cgpa=9.20,
            attendance_percentage=96.8
        )
        self._students[stu2.id] = stu2

    async def get_by_id(self, student_id: str) -> Optional[Student]:
        return self._students.get(student_id)

    async def get_by_email(self, email: str) -> Optional[Student]:
        for s in self._students.values():
            if s.email.lower() == email.lower():
                return s
        return None

    async def list_students(self, department_id: Optional[str] = None) -> List[Student]:
        if department_id:
            return [s for s in self._students.values() if s.department_id == department_id]
        return list(self._students.values())

    async def save(self, student: Student) -> Student:
        self._students[student.id] = student
        return student

default_student_repo = InMemoryStudentRepository()
