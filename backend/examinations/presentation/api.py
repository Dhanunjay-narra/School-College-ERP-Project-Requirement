"""
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
