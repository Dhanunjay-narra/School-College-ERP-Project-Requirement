"""
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
