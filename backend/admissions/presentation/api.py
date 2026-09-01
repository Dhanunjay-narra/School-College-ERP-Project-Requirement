"""
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
