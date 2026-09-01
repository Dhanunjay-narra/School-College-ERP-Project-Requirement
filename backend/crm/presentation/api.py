"""
CRM & Alumni Network Management API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/crm", tags=["CRM & Alumni Platform"])

class AlumniMember(BaseModel):
    id: str
    full_name: str
    graduating_class: int
    program: str
    current_company: str
    designation: str
    location: str

@router.get("/alumni", response_model=List[AlumniMember])
async def list_alumni():
    return [
        AlumniMember(id="ALUM-2022-01", full_name="Siddharth Rao", graduating_class=2022, program="B.Tech CSE", current_company="Google", designation="Senior Software Engineer", location="Bengaluru, India"),
        AlumniMember(id="ALUM-2021-04", full_name="Sneha Kulkarni", graduating_class=2021, program="B.Tech ECE", current_company="Qualcomm", designation="Hardware Systems Architect", location="Hyderabad, India"),
    ]
