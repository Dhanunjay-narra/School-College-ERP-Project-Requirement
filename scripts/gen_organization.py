from writer_util import write_f

def build_organization():
    print("[PHASE 03] Building Organization & Multi-Tenancy Module...")

    write_f("backend/organization/__init__.py", '"""Organization & Multi-Campus Management Package."""\n')
    write_f("backend/organization/domain/__init__.py", "")
    write_f("backend/organization/application/__init__.py", "")
    write_f("backend/organization/infrastructure/__init__.py", "")
    write_f("backend/organization/presentation/__init__.py", "")

    write_f("backend/organization/domain/value_objects.py", '''"""
Organization Domain Value Objects.
"""
from enum import Enum

class InstitutionType(str, Enum):
    SCHOOL = "SCHOOL"
    COLLEGE = "COLLEGE"
    UNIVERSITY = "UNIVERSITY"
    AFFILIATED_COLLEGE = "AFFILIATED_COLLEGE"
    POLYTECHNIC = "POLYTECHNIC"

class RoomType(str, Enum):
    CLASSROOM = "CLASSROOM"
    LABORATORY = "LABORATORY"
    LECTURE_HALL = "LECTURE_HALL"
    SEMINAR_HALL = "SEMINAR_HALL"
    FACULTY_OFFICE = "FACULTY_OFFICE"
    AUDITORIUM = "AUDITORIUM"
    LIBRARY = "LIBRARY"
    STORE_ROOM = "STORE_ROOM"
    CAFETERIA = "CAFETERIA"

class DepartmentType(str, Enum):
    ACADEMIC = "ACADEMIC"
    ADMINISTRATIVE = "ADMINISTRATIVE"
    FINANCE = "FINANCE"
    HUMAN_RESOURCES = "HUMAN_RESOURCES"
    EXAMINATION_CELL = "EXAMINATION_CELL"
    STUDENT_AFFAIRS = "STUDENT_AFFAIRS"
    TRANSPORT = "TRANSPORT"
    HOSTEL = "HOSTEL"
    LIBRARY = "LIBRARY"
    IT_SERVICES = "IT_SERVICES"
    PROCUREMENT = "PROCUREMENT"
''')

    write_f("backend/organization/domain/entities.py", '''"""
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
''')

    write_f("backend/organization/infrastructure/repositories.py", '''"""
Organization In-Memory Repository with Seed Data.
"""
from typing import List, Optional, Dict
import uuid
from backend.organization.domain.entities import Institution, Campus, Building, Room, Department
from backend.organization.domain.value_objects import InstitutionType, RoomType, DepartmentType

class InMemoryOrganizationRepository:
    def __init__(self):
        self.institutions: Dict[str, Institution] = {}
        self.campuses: Dict[str, Campus] = {}
        self.buildings: Dict[str, Building] = {}
        self.rooms: Dict[str, Room] = {}
        self.departments: Dict[str, Department] = {}
        self._seed_data()

    def _seed_data(self):
        inst_id = "default_institution"
        inst = Institution(
            id=inst_id,
            name="Apex Institute of Technology & Management",
            code="AITM",
            institution_type=InstitutionType.UNIVERSITY,
            accreditation="NAAC A++ Grade, NBA, ISO 9001:2015",
            affiliation="Apex Technical University",
            address="Knowledge Corridor, Sector 62, Tech City"
        )
        self.institutions[inst_id] = inst

        campus_id = "MAIN-CAMPUS"
        campus = Campus(
            id=campus_id,
            institution_id=inst_id,
            name="Main Academic Campus",
            code="MAIN",
            address="Plot 1-4, University Road",
            city="Tech City",
            state="Telangana",
            is_main_campus=True
        )
        self.campuses[campus_id] = campus

        bld_id = "BLD-TECH-01"
        bld = Building(id=bld_id, campus_id=campus_id, name="Aryabhata Computing Block", code="ACB", total_floors=5)
        self.buildings[bld_id] = bld

        # Seed Rooms
        room1 = Room(id="RM-101", building_id=bld_id, room_number="101", floor_number=1, room_type=RoomType.CLASSROOM, seating_capacity=70)
        room2 = Room(id="LAB-201", building_id=bld_id, room_number="201", floor_number=2, room_type=RoomType.LABORATORY, seating_capacity=45)
        self.rooms[room1.id] = room1
        self.rooms[room2.id] = room2

        # Seed Departments
        dept_data = [
            ("CS-DEP", "Computer Science & Engineering", "CSE", DepartmentType.ACADEMIC),
            ("ECE-DEP", "Electronics & Communication Engineering", "ECE", DepartmentType.ACADEMIC),
            ("MECH-DEP", "Mechanical & Mechatronics Engineering", "MECH", DepartmentType.ACADEMIC),
            ("ADMIN-DEP", "Executive Administration", "ADMIN", DepartmentType.ADMINISTRATIVE),
            ("FIN-DEP", "Finance & Accounts Department", "FIN", DepartmentType.FINANCE),
            ("HR-DEP", "Human Resource & Payroll", "HR", DepartmentType.HUMAN_RESOURCES),
            ("LIB-DEP", "Central Digital Library", "LIB", DepartmentType.LIBRARY),
            ("HOSTEL-DEP", "Hostel & Housing Administration", "HOSTEL", DepartmentType.HOSTEL),
            ("TRANS-DEP", "Transport & Fleet Operations", "TRANS", DepartmentType.TRANSPORT),
            ("EXAM-DEP", "Examination & Evaluation Cell", "EXAM", DepartmentType.EXAMINATION_CELL),
        ]
        for d_id, name, code, d_type in dept_data:
            dept = Department(
                id=d_id,
                institution_id=inst_id,
                campus_id=campus_id,
                name=name,
                code=code,
                department_type=d_type,
                email=f"{code.lower()}@erp.edu"
            )
            self.departments[dept.id] = dept

    async def get_institution(self, inst_id: str) -> Optional[Institution]:
        return self.institutions.get(inst_id)

    async def list_campuses(self, inst_id: str) -> List[Campus]:
        return [c for c in self.campuses.values() if c.institution_id == inst_id]

    async def list_departments(self, inst_id: str) -> List[Department]:
        return [d for d in self.departments.values() if d.institution_id == inst_id]

    async def list_rooms(self) -> List[Room]:
        return list(self.rooms.values())

default_org_repo = InMemoryOrganizationRepository()
''')

    write_f("backend/organization/presentation/schemas.py", '''"""
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
''')

    write_f("backend/organization/presentation/api.py", '''"""
Organization API Endpoints.
"""
from fastapi import APIRouter, HTTPException
from typing import List
from backend.organization.presentation.schemas import InstitutionResponse, CampusResponse, DepartmentResponse, RoomResponse
from backend.organization.infrastructure.repositories import default_org_repo

router = APIRouter(prefix="/organization", tags=["Organization & Multi-Campus"])

@router.get("/institution", response_model=InstitutionResponse)
async def get_institution():
    """Get active institution details."""
    inst = await default_org_repo.get_institution("default_institution")
    if not inst:
        raise HTTPException(status_code=404, detail="Institution not found")
    return InstitutionResponse(
        id=inst.id,
        name=inst.name,
        code=inst.code,
        institution_type=inst.institution_type.value,
        accreditation=inst.accreditation,
        affiliation=inst.affiliation,
        currency=inst.currency,
        timezone=inst.timezone,
        contact_email=inst.contact_email,
        contact_phone=inst.contact_phone,
        address=inst.address
    )

@router.get("/campuses", response_model=List[CampusResponse])
async def list_campuses():
    """List institution campuses."""
    campuses = await default_org_repo.list_campuses("default_institution")
    return [
        CampusResponse(
            id=c.id,
            name=c.name,
            code=c.code,
            city=c.city,
            state=c.state,
            is_main_campus=c.is_main_campus
        )
        for c in campuses
    ]

@router.get("/departments", response_model=List[DepartmentResponse])
async def list_departments():
    """List academic and administrative departments."""
    depts = await default_org_repo.list_departments("default_institution")
    return [
        DepartmentResponse(
            id=d.id,
            name=d.name,
            code=d.code,
            department_type=d.department_type.value,
            email=d.email
        )
        for d in depts
    ]

@router.get("/rooms", response_model=List[RoomResponse])
async def list_rooms():
    """List campus facilities and classrooms."""
    rooms = await default_org_repo.list_rooms()
    return [
        RoomResponse(
            id=r.id,
            building_id=r.building_id,
            room_number=r.room_number,
            floor_number=r.floor_number,
            room_type=r.room_type.value,
            seating_capacity=r.seating_capacity,
            has_projector=r.has_projector,
            is_air_conditioned=r.is_air_conditioned
        )
        for r in rooms
    ]
''')

    print("[GEN] Organization & Multi-Tenancy Module complete.")

if __name__ == '__main__':
    build_organization()
