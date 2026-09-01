"""
Student Domain Entities.
"""
import uuid
from datetime import date, datetime
from typing import Optional, List
from backend.students.domain.value_objects import StudentStatus, Gender, BloodGroup

class Student:
    def __init__(
        self,
        id: str,
        user_id: str,
        admission_number: str,
        roll_number: str,
        first_name: str,
        last_name: str,
        date_of_birth: date,
        gender: Gender,
        email: str,
        phone_number: str,
        department_id: str,
        program_id: str,
        current_semester: int = 1,
        section: str = "A",
        status: StudentStatus = StudentStatus.ACTIVE,
        blood_group: BloodGroup = BloodGroup.O_POSITIVE,
        address: str = "123 Academic Enclave",
        emergency_contact_name: str = "Vikram Sharma",
        emergency_contact_phone: str = "+91-9876543201",
        cgpa: float = 8.75,
        attendance_percentage: float = 92.5,
        created_at: Optional[datetime] = None
    ):
        self.id = id or str(uuid.uuid4())
        self.user_id = user_id
        self.admission_number = admission_number
        self.roll_number = roll_number
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email = email.lower()
        self.phone_number = phone_number
        self.department_id = department_id
        self.program_id = program_id
        self.current_semester = current_semester
        self.section = section
        self.status = status
        self.blood_group = blood_group
        self.address = address
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone
        self.cgpa = cgpa
        self.attendance_percentage = attendance_percentage
        self.created_at = created_at or datetime.utcnow()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def transition_status(self, new_status: StudentStatus):
        self.status = new_status
