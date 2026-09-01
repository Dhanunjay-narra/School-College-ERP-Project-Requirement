"""
Campus Infrastructure Projects and Event Management API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/projects-events", tags=["Projects & Event Management"])

class CampusEvent(BaseModel):
    id: str
    title: str
    category: str
    date: str
    venue: str
    registered_participants: int
    status: str

@router.get("/events", response_model=List[CampusEvent])
async def list_events():
    return [
        CampusEvent(id="EVT-2026-01", title="International Conference on AI & Autonomous Systems (ICAAS 2026)", category="Academic Conference", date="2026-10-15", venue="Main University Auditorium", registered_participants=420, status="REGISTRATIONS_OPEN"),
        CampusEvent(id="EVT-2026-02", title="Apex National Hackathon: Smart Campus Solutions", category="Technical Competition", date="2026-09-25", venue="Aryabhata Innovation Hub", registered_participants=350, status="REGISTRATIONS_OPEN"),
    ]
