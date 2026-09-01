"""
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
