"""
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
