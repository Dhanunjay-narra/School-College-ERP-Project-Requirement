"""
Universal Reporting Engine API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/reports", tags=["Reporting Platform"])

class ReportTemplate(BaseModel):
    id: str
    name: str
    category: str
    supported_formats: List[str]
    last_generated: str

@router.get("/templates", response_model=List[ReportTemplate])
async def list_report_templates():
    return [
        ReportTemplate(id="REP-01", name="Comprehensive Student Semester Academic Performance", category="ACADEMICS", supported_formats=["PDF", "EXCEL", "CSV"], last_generated="2026-08-30"),
        ReportTemplate(id="REP-02", name="Consolidated Fee Invoicing & Outstanding Dues Statement", category="FINANCE", supported_formats=["PDF", "EXCEL"], last_generated="2026-08-31"),
        ReportTemplate(id="REP-03", name="Monthly Employee Payroll Disbursement & Tax Deduction Summary", category="HR_PAYROLL", supported_formats=["PDF", "EXCEL"], last_generated="2026-08-31"),
    ]
