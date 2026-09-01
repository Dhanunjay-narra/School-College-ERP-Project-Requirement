"""
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
