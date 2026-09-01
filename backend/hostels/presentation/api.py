"""
Hostel, Room Allocation, Mess & Outpass API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/hostels", tags=["Hostel Management"])

class HostelRoom(BaseModel):
    hostel_block: str
    room_number: str
    floor: int
    total_beds: int
    occupied_beds: int
    ac_available: bool

@router.get("/rooms", response_model=List[HostelRoom])
async def list_hostel_rooms():
    return [
        HostelRoom(hostel_block="Tagore Boys Residence (Block A)", room_number="A-304", floor=3, total_beds=2, occupied_beds=2, ac_available=True),
        HostelRoom(hostel_block="Sarojini Girls Residence (Block B)", room_number="B-201", floor=2, total_beds=2, occupied_beds=1, ac_available=True),
    ]
