from writer_util import write_f

def build_education_domains():
    print("[PHASES 04-11] Generating Education & Academic Domains...")

    # Phase 04: Students
    write_f("backend/students/__init__.py", "")
    write_f("backend/students/domain/__init__.py", "")
    write_f("backend/students/domain/value_objects.py", '''"""
Student Domain Value Objects.
"""
from enum import Enum

class StudentStatus(str, Enum):
    ENQUIRY = "ENQUIRY"
    APPLICANT = "APPLICANT"
    APPLICATION_SUBMITTED = "APPLICATION_SUBMITTED"
    SHORTLISTED = "SHORTLISTED"
    ADMITTED = "ADMITTED"
    ENROLLED = "ENROLLED"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    WITHDRAWN = "WITHDRAWN"
    TRANSFERRED = "TRANSFERRED"
    GRADUATED = "GRADUATED"
    ALUMNI = "ALUMNI"

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

class BloodGroup(str, Enum):
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
''')

    write_f("backend/students/domain/entities.py", '''"""
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
''')

    write_f("backend/students/infrastructure/repositories.py", '''"""
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
''')

    write_f("backend/students/presentation/api.py", '''"""
Student Management API Routes.
"""
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from backend.students.infrastructure.repositories import default_student_repo

router = APIRouter(prefix="/students", tags=["Student Management"])

class StudentResponse(BaseModel):
    id: str
    admission_number: str
    roll_number: str
    first_name: str
    last_name: str
    full_name: str
    email: str
    phone_number: str
    department_id: str
    program_id: str
    current_semester: int
    section: str
    status: str
    cgpa: float
    attendance_percentage: float

@router.get("/", response_model=List[StudentResponse])
async def list_students(department_id: Optional[str] = None):
    students = await default_student_repo.list_students(department_id)
    return [
        StudentResponse(
            id=s.id,
            admission_number=s.admission_number,
            roll_number=s.roll_number,
            first_name=s.first_name,
            last_name=s.last_name,
            full_name=s.full_name,
            email=s.email,
            phone_number=s.phone_number,
            department_id=s.department_id,
            program_id=s.program_id,
            current_semester=s.current_semester,
            section=s.section,
            status=s.status.value,
            cgpa=s.cgpa,
            attendance_percentage=s.attendance_percentage
        )
        for s in students
    ]

@router.get("/{student_id}", response_model=StudentResponse)
async def get_student(student_id: str):
    s = await default_student_repo.get_by_id(student_id)
    if not s:
        raise HTTPException(status_code=404, detail="Student not found")
    return StudentResponse(
        id=s.id,
        admission_number=s.admission_number,
        roll_number=s.roll_number,
        first_name=s.first_name,
        last_name=s.last_name,
        full_name=s.full_name,
        email=s.email,
        phone_number=s.phone_number,
        department_id=s.department_id,
        program_id=s.program_id,
        current_semester=s.current_semester,
        section=s.section,
        status=s.status.value,
        cgpa=s.cgpa,
        attendance_percentage=s.attendance_percentage
    )
''')

    # Phase 05: Parents & Guardians
    write_f("backend/parents/__init__.py", "")
    write_f("backend/parents/presentation/api.py", '''"""
Parent & Guardian Portal API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/parents", tags=["Parent & Guardian Management"])

class ParentProfile(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    relation: str
    ward_student_id: str
    ward_name: str
    fee_responsibility: bool

@router.get("/profile")
async def get_parent_profile():
    return ParentProfile(
        id="PAR-001",
        first_name="Vikram",
        last_name="Sharma",
        email="parent.sharma@erp.edu",
        phone_number="+91-9876543201",
        relation="Father",
        ward_student_id="STU-2026-001",
        ward_name="Aarav Patel",
        fee_responsibility=True
    )
''')

    # Phase 06: Admissions Management CRM
    write_f("backend/admissions/__init__.py", "")
    write_f("backend/admissions/presentation/api.py", '''"""
Admissions CRM API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/admissions", tags=["Admissions Management CRM"])

class AdmissionApplication(BaseModel):
    id: str
    candidate_name: str
    program: str
    entrance_score: float
    status: str
    category: str
    applied_date: str

@router.get("/applications", response_model=List[AdmissionApplication])
async def list_applications():
    return [
        AdmissionApplication(id="APP-2026-101", candidate_name="Rohan Gupta", program="B.Tech CS", entrance_score=94.5, status="OFFER_LETTER_SENT", category="GENERAL", applied_date="2026-08-10"),
        AdmissionApplication(id="APP-2026-102", candidate_name="Pooja Sen", program="B.Tech ECE", entrance_score=88.0, status="DOCUMENT_VERIFIED", category="OBC", applied_date="2026-08-12"),
        AdmissionApplication(id="APP-2026-103", candidate_name="Karan Verma", program="MBA Finance", entrance_score=91.2, status="INTERVIEW_SCHEDULED", category="GENERAL", applied_date="2026-08-15"),
    ]
''')

    # Phase 07: Academic Management & Timetable
    write_f("backend/academics/__init__.py", "")
    write_f("backend/academics/presentation/api.py", '''"""
Academic Programs, Courses, Subjects, and Timetable API.
"""
from fastapi import APIRouter
from typing import List, Dict, Any
from pydantic import BaseModel

router = APIRouter(prefix="/academics", tags=["Academic Structure & Timetable"])

class CourseItem(BaseModel):
    code: str
    title: str
    credits: int
    department: str
    faculty_in_charge: str
    semester: int

class TimetableSlot(BaseModel):
    day: str
    time: str
    subject: str
    subject_code: str
    faculty: str
    room: str

@router.get("/courses", response_model=List[CourseItem])
async def list_courses():
    return [
        CourseItem(code="CS401", title="Distributed Systems & Cloud Computing", credits=4, department="CSE", faculty_in_charge="Dr. David Smith", semester=4),
        CourseItem(code="CS402", title="Artificial Intelligence & Machine Learning", credits=4, department="CSE", faculty_in_charge="Prof. Ananya Iyer", semester=4),
        CourseItem(code="CS403", title="Database Engineering & Big Data", credits=3, department="CSE", faculty_in_charge="Dr. Sarah Jenkins", semester=4),
        CourseItem(code="CS404", title="Software Architecture & Design Patterns", credits=3, department="CSE", faculty_in_charge="Prof. Michael Chang", semester=4),
    ]

@router.get("/timetable", response_model=List[TimetableSlot])
async def get_timetable():
    return [
        TimetableSlot(day="Monday", time="09:00 - 10:00", subject="Distributed Systems", subject_code="CS401", faculty="Dr. David Smith", room="RM-101"),
        TimetableSlot(day="Monday", time="10:00 - 11:00", subject="Artificial Intelligence", subject_code="CS402", faculty="Prof. Ananya Iyer", room="RM-101"),
        TimetableSlot(day="Tuesday", time="09:00 - 10:00", subject="Database Engineering", subject_code="CS403", faculty="Dr. Sarah Jenkins", room="LAB-201"),
        TimetableSlot(day="Wednesday", time="11:15 - 12:15", subject="Software Architecture", subject_code="CS404", faculty="Prof. Michael Chang", room="RM-101"),
    ]
''')

    # Phase 08: Faculty Management
    write_f("backend/faculty/__init__.py", "")
    write_f("backend/faculty/presentation/api.py", '''"""
Faculty Management & Workload Balancing API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/faculty", tags=["Faculty Management"])

class FacultyMember(BaseModel):
    id: str
    name: str
    designation: str
    department: str
    qualification: str
    teaching_hours_per_week: int
    lab_hours_per_week: int
    research_projects: int
    publications: int

@router.get("/", response_model=List[FacultyMember])
async def list_faculty():
    return [
        FacultyMember(id="FAC-001", name="Dr. David Smith", designation="Professor & Researcher", department="CSE", qualification="Ph.D. in Distributed Computing", teaching_hours_per_week=12, lab_hours_per_week=6, research_projects=3, publications=18),
        FacultyMember(id="FAC-002", name="Prof. Ananya Iyer", designation="Head of Department & Professor", department="CSE", qualification="Ph.D. in AI & Robotics", teaching_hours_per_week=8, lab_hours_per_week=4, research_projects=5, publications=24),
        FacultyMember(id="FAC-003", name="Dr. Sarah Jenkins", designation="Associate Professor", department="CSE", qualification="Ph.D. in Database Systems", teaching_hours_per_week=14, lab_hours_per_week=8, research_projects=2, publications=11),
    ]
''')

    # Phase 09: Attendance Management
    write_f("backend/attendance/__init__.py", "")
    write_f("backend/attendance/presentation/api.py", '''"""
Smart Attendance Engine API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/attendance", tags=["Attendance Management"])

class AttendanceRecord(BaseModel):
    date: str
    subject: str
    status: str
    marked_by: str
    method: str

class AttendanceSummary(BaseModel):
    total_classes: int
    attended_classes: int
    percentage: float
    status: str

@router.get("/summary", response_model=AttendanceSummary)
async def get_student_attendance_summary():
    return AttendanceSummary(total_classes=120, attended_classes=113, percentage=94.17, status="EXEMPLARY")

@router.get("/logs", response_model=List[AttendanceRecord])
async def get_attendance_logs():
    return [
        AttendanceRecord(date="2026-08-31", subject="Distributed Systems", status="PRESENT", marked_by="Dr. David Smith", method="BIOMETRIC_SMART_GATE"),
        AttendanceRecord(date="2026-08-31", subject="Artificial Intelligence", status="PRESENT", marked_by="Prof. Ananya Iyer", method="FACULTY_APP_QR"),
        AttendanceRecord(date="2026-08-30", subject="Database Engineering", status="PRESENT", marked_by="Dr. Sarah Jenkins", method="SMART_GATEWAY"),
        AttendanceRecord(date="2026-08-29", subject="Software Architecture", status="LATE", marked_by="Prof. Michael Chang", method="FACULTY_APP_QR"),
    ]
''')

    # Phase 10: Examination & Transcripts
    write_f("backend/examinations/__init__.py", "")
    write_f("backend/examinations/presentation/api.py", '''"""
Examination Management, Moderation, and Grading API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/examinations", tags=["Examination Management"])

class ExamSchedule(BaseModel):
    id: str
    exam_name: str
    subject: str
    subject_code: str
    date: str
    time: str
    hall: str
    invigilator: str

class GradeItem(BaseModel):
    subject_code: str
    subject_name: str
    credits: int
    internal_marks: float
    end_sem_marks: float
    total_marks: float
    grade: str
    grade_point: float

@router.get("/schedules", response_model=List[ExamSchedule])
async def list_exam_schedules():
    return [
        ExamSchedule(id="EX-401", exam_name="Midterm Examination - Fall 2026", subject="Distributed Systems", subject_code="CS401", date="2026-09-15", time="10:00 - 12:00", hall="Exam Hall A", invigilator="Dr. K. Venkatesh"),
        ExamSchedule(id="EX-402", exam_name="Midterm Examination - Fall 2026", subject="Artificial Intelligence", subject_code="CS402", date="2026-09-17", time="10:00 - 12:00", hall="Exam Hall B", invigilator="Dr. Rajesh Sharma"),
    ]

@router.get("/grades", response_model=List[GradeItem])
async def get_student_grades():
    return [
        GradeItem(subject_code="CS401", subject_name="Distributed Systems", credits=4, internal_marks=28.5, end_sem_marks=62.0, total_marks=90.5, grade="A+", grade_point=10.0),
        GradeItem(subject_code="CS402", subject_name="Artificial Intelligence", credits=4, internal_marks=27.0, end_sem_marks=59.0, total_marks=86.0, grade="A", grade_point=9.0),
        GradeItem(subject_code="CS403", subject_name="Database Engineering", credits=3, internal_marks=29.0, end_sem_marks=60.0, total_marks=89.0, grade="A+", grade_point=10.0),
    ]
''')

    # Phase 11: Assignments & LMS
    write_f("backend/assignments/__init__.py", "")
    write_f("backend/assignments/presentation/api.py", '''"""
Assignments & Learning Management System API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/assignments", tags=["Assignments & LMS"])

class Assignment(BaseModel):
    id: str
    title: str
    subject: str
    due_date: str
    max_marks: int
    status: str
    submission_count: int

@router.get("/", response_model=List[Assignment])
async def list_assignments():
    return [
        Assignment(id="ASN-001", title="Raft Consensus Algorithm Implementation", subject="Distributed Systems (CS401)", due_date="2026-09-10", max_marks=50, status="SUBMITTED", submission_count=42),
        Assignment(id="ASN-002", title="Convolutional Neural Network for Image Recognition", subject="Artificial Intelligence (CS402)", due_date="2026-09-14", max_marks=100, status="PENDING", submission_count=28),
        Assignment(id="ASN-003", title="B-Tree Indexing Optimization", subject="Database Engineering (CS403)", due_date="2026-09-20", max_marks=50, status="GRADED", submission_count=45),
    ]
''')

    print("[GEN] Education & Academic domains complete.")

if __name__ == '__main__':
    build_education_domains()
