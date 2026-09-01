"""
Universal Multi-Channel Communication Platform API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/communication", tags=["Universal Communication Platform"])

class CircularNotice(BaseModel):
    id: str
    title: str
    category: str
    priority: str
    publish_date: str
    channels: List[str]
    content: str

@router.get("/notices", response_model=List[CircularNotice])
async def list_notices():
    return [
        CircularNotice(id="CIR-2026-44", title="Midterm Examination Schedule Released - Fall 2026", category="EXAMINATIONS", priority="HIGH", publish_date="2026-08-30", channels=["EMAIL", "SMS", "IN_APP", "WHATSAPP"], content="All students are requested to download hall tickets from the student portal before September 10, 2026."),
        CircularNotice(id="CIR-2026-45", title="Annual Technical Fest & Hackathon Registrations Open", category="CAMPUS_LIFE", priority="NORMAL", publish_date="2026-08-28", channels=["IN_APP", "EMAIL"], content="Register your project teams before September 15 for the upcoming National Smart Campus Hackathon."),
    ]
