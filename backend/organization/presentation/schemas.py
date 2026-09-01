"""
Organization Request/Response Schemas.
"""
from typing import List, Optional
from pydantic import BaseModel

class InstitutionResponse(BaseModel):
    id: str
    name: str
    code: str
    institution_type: str
    accreditation: str
    affiliation: str
    currency: str
    timezone: str
    contact_email: str
    contact_phone: str
    address: str

class CampusResponse(BaseModel):
    id: str
    name: str
    code: str
    city: str
    state: str
    is_main_campus: bool

class DepartmentResponse(BaseModel):
    id: str
    name: str
    code: str
    department_type: str
    email: Optional[str] = None

class RoomResponse(BaseModel):
    id: str
    building_id: str
    room_number: str
    floor_number: int
    room_type: str
    seating_capacity: int
    has_projector: bool
    is_air_conditioned: bool
