from writer_util import write_f

def build_operations_hr():
    print("[PHASES 17-21, 26-27] Generating Operations, HR, Payroll, Transport, Hostel, Library & Research...")

    # Phase 17: HR Management
    write_f("backend/hr/__init__.py", "")
    write_f("backend/hr/presentation/api.py", '''"""
Human Resource Management, Recruitment, and Leave Management API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/hr", tags=["HR Management & Recruitment"])

class Employee(BaseModel):
    id: str
    employee_code: str
    full_name: str
    department: str
    designation: str
    joining_date: str
    employment_type: str
    leave_balance_casual: int
    leave_balance_earned: int
    status: str

@router.get("/employees", response_model=List[Employee])
async def list_employees():
    return [
        Employee(id="EMP-001", employee_code="FAC-CS-01", full_name="Dr. David Smith", department="Computer Science", designation="Professor", joining_date="2018-06-15", employment_type="REGULAR_FULLTIME", leave_balance_casual=8, leave_balance_earned=14, status="ACTIVE"),
        Employee(id="EMP-002", employee_code="FAC-CS-02", full_name="Prof. Ananya Iyer", department="Computer Science", designation="Head of Department", joining_date="2016-01-10", employment_type="REGULAR_FULLTIME", leave_balance_casual=6, leave_balance_earned=18, status="ACTIVE"),
        Employee(id="EMP-003", employee_code="STAFF-FIN-01", full_name="Priya Nair", department="Finance", designation="Chief Accountant", joining_date="2020-03-01", employment_type="REGULAR_FULLTIME", leave_balance_casual=10, leave_balance_earned=12, status="ACTIVE"),
    ]
''')

    # Phase 18: Payroll
    write_f("backend/payroll/__init__.py", "")
    write_f("backend/payroll/presentation/api.py", '''"""
Integrated Payroll & Compensation Management API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/payroll", tags=["Payroll Management"])

class Payslip(BaseModel):
    payslip_id: str
    employee_code: str
    employee_name: str
    month_year: str
    basic_salary: float
    allowances_hra_da: float
    deductions_pf_tds: float
    net_salary: float
    status: str

@router.get("/payslips", response_model=List[Payslip])
async def list_payslips():
    return [
        Payslip(payslip_id="PAY-2026-08-01", employee_code="FAC-CS-01", employee_name="Dr. David Smith", month_year="August 2026", basic_salary=110000.0, allowances_hra_da=45000.0, deductions_pf_tds=22000.0, net_salary=133000.0, status="DISBURSED"),
        Payslip(payslip_id="PAY-2026-08-02", employee_code="FAC-CS-02", employee_name="Prof. Ananya Iyer", month_year="August 2026", basic_salary=125000.0, allowances_hra_da=50000.0, deductions_pf_tds=26000.0, net_salary=149000.0, status="DISBURSED"),
        Payslip(payslip_id="PAY-2026-08-03", employee_code="STAFF-FIN-01", employee_name="Priya Nair", month_year="August 2026", basic_salary=75000.0, allowances_hra_da=30000.0, deductions_pf_tds=14000.0, net_salary=91000.0, status="DISBURSED"),
    ]
''')

    # Phase 19: Transportation Management
    write_f("backend/transport/__init__.py", "")
    write_f("backend/transport/presentation/api.py", '''"""
Transport Fleet, Routes, GPS Tracking & Stops API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/transport", tags=["Transportation Management"])

class BusRoute(BaseModel):
    route_id: str
    route_name: str
    bus_number: str
    driver_name: str
    driver_phone: str
    total_capacity: int
    assigned_students: int
    current_status: str
    live_lat: float
    live_lng: float

@router.get("/routes", response_model=List[BusRoute])
async def list_routes():
    return [
        BusRoute(route_id="RT-01", route_name="North Corridor - Tech Campus Express", bus_number="AP-29-BD-1001", driver_name="Gurpreet Singh", driver_phone="+91-9876541101", total_capacity=52, assigned_students=48, current_status="ON_ROUTE", live_lat=17.4400, live_lng=78.3489),
        BusRoute(route_id="RT-02", route_name="South City Ring Road Line", bus_number="AP-29-BD-1002", driver_name="Mahesh Yadav", driver_phone="+91-9876541102", total_capacity=52, assigned_students=44, current_status="AT_CAMPUS", live_lat=17.4455, live_lng=78.3520),
    ]
''')

    # Phase 20: Hostel Management
    write_f("backend/hostels/__init__.py", "")
    write_f("backend/hostels/presentation/api.py", '''"""
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
''')

    # Phase 21: Library Management
    write_f("backend/library/__init__.py", "")
    write_f("backend/library/presentation/api.py", '''"""
Library MARC21/ISBN Catalog & RFID Circulation API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/library", tags=["Library Management"])

class LibraryBook(BaseModel):
    isbn: str
    title: str
    authors: str
    category: str
    total_copies: int
    available_copies: int
    shelf_location: str

@router.get("/books", response_model=List[LibraryBook])
async def list_books():
    return [
        LibraryBook(isbn="978-0134494166", title="Designing Data-Intensive Applications", authors="Martin Kleppmann", category="Computer Science", total_copies=12, available_copies=5, shelf_location="Shelf CS-12A"),
        LibraryBook(isbn="978-0262033848", title="Introduction to Algorithms (4th Edition)", authors="Cormen, Leiserson, Rivest, Stein", category="Algorithms", total_copies=25, available_copies=14, shelf_location="Shelf CS-04B"),
        LibraryBook(isbn="978-0132350884", title="Clean Code: A Handbook of Agile Software Craftsmanship", authors="Robert C. Martin", category="Software Engineering", total_copies=18, available_copies=8, shelf_location="Shelf CS-08C"),
    ]
''')

    # Phase 26: Project & Campus Events
    write_f("backend/projects/__init__.py", "")
    write_f("backend/projects/presentation/api.py", '''"""
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
''')

    # Phase 27: Research & Innovation
    write_f("backend/research/__init__.py", "")
    write_f("backend/research/presentation/api.py", '''"""
Research Projects, Grants, Publications & Patents API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/research", tags=["Research & Innovation Management"])

class ResearchGrant(BaseModel):
    grant_id: str
    project_title: str
    principal_investigator: str
    funding_agency: str
    sanctioned_amount: float
    disbursed_amount: float
    duration_months: int
    status: str

@router.get("/grants", response_model=List[ResearchGrant])
async def list_research_grants():
    return [
        ResearchGrant(grant_id="DST-SERB-2025-44", project_title="Edge AI for Smart Grid Energy Management", principal_investigator="Dr. David Smith", funding_agency="DST-SERB / Govt of India", sanctioned_amount=4500000.0, disbursed_amount=3000000.0, duration_months=36, status="IN_PROGRESS"),
        ResearchGrant(grant_id="ISRO-RESP-2025-12", project_title="Autonomous Satellite Imagery Analysis for Climate Tracking", principal_investigator="Prof. Ananya Iyer", funding_agency="ISRO / DOS", sanctioned_amount=6200000.0, disbursed_amount=4000000.0, duration_months=24, status="IN_PROGRESS"),
    ]
''')

    print("[GEN] Operations, HR, Payroll, Transport, Hostel, Library & Research complete.")

if __name__ == '__main__':
    build_operations_hr()
