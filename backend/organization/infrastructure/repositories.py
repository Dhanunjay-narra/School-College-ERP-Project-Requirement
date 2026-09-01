"""
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
