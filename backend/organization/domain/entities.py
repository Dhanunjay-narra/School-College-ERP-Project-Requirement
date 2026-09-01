"""
Organization Domain Entities.
"""
import uuid
from typing import List, Optional
from datetime import datetime, date
from backend.organization.domain.value_objects import InstitutionType, RoomType, DepartmentType

class Institution:
    def __init__(
        self,
        id: str,
        name: str,
        code: str,
        institution_type: InstitutionType,
        accreditation: str = "NAAC A++ / NBA Accredited",
        affiliation: str = "State Technical University",
        currency: str = "INR",
        timezone: str = "Asia/Kolkata",
        website: str = "https://erp.edu",
        contact_email: str = "contact@erp.edu",
        contact_phone: str = "+91-11-23456789",
        address: str = "Institutional Area, Knowledge Park",
        created_at: Optional[datetime] = None
    ):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.code = code.upper()
        self.institution_type = institution_type
        self.accreditation = accreditation
        self.affiliation = affiliation
        self.currency = currency
        self.timezone = timezone
        self.website = website
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.address = address
        self.created_at = created_at or datetime.utcnow()

class Campus:
    def __init__(
        self,
        id: str,
        institution_id: str,
        name: str,
        code: str,
        address: str,
        city: str,
        state: str,
        country: str = "India",
        pincode: str = "500001",
        is_main_campus: bool = False
    ):
        self.id = id or str(uuid.uuid4())
        self.institution_id = institution_id
        self.name = name
        self.code = code.upper()
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.pincode = pincode
        self.is_main_campus = is_main_campus

class Building:
    def __init__(
        self,
        id: str,
        campus_id: str,
        name: str,
        code: str,
        total_floors: int = 4,
        description: str = ""
    ):
        self.id = id or str(uuid.uuid4())
        self.campus_id = campus_id
        self.name = name
        self.code = code.upper()
        self.total_floors = total_floors
        self.description = description

class Room:
    def __init__(
        self,
        id: str,
        building_id: str,
        room_number: str,
        floor_number: int,
        room_type: RoomType,
        seating_capacity: int = 60,
        has_projector: bool = True,
        is_air_conditioned: bool = True
    ):
        self.id = id or str(uuid.uuid4())
        self.building_id = building_id
        self.room_number = room_number
        self.floor_number = floor_number
        self.room_type = room_type
        self.seating_capacity = seating_capacity
        self.has_projector = has_projector
        self.is_air_conditioned = is_air_conditioned

class Department:
    def __init__(
        self,
        id: str,
        institution_id: str,
        campus_id: str,
        name: str,
        code: str,
        department_type: DepartmentType,
        hod_id: Optional[str] = None,
        email: Optional[str] = None
    ):
        self.id = id or str(uuid.uuid4())
        self.institution_id = institution_id
        self.campus_id = campus_id
        self.name = name
        self.code = code.upper()
        self.department_type = department_type
        self.hod_id = hod_id
        self.email = email
