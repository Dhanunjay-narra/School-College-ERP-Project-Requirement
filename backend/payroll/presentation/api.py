"""
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
