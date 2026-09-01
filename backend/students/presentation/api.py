"""
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
