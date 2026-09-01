"""
Fee Structure, Billing, Invoicing & Scholarships API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/fees", tags=["Fees & Student Billing"])

class FeeInvoice(BaseModel):
    invoice_number: str
    student_id: str
    student_name: str
    description: str
    amount_due: float
    amount_paid: float
    balance: float
    due_date: str
    status: str

@router.get("/invoices", response_model=List[FeeInvoice])
async def list_invoices():
    return [
        FeeInvoice(invoice_number="INV-2026-8801", student_id="STU-2026-001", student_name="Aarav Patel", description="Academic Year 2026-27 Tuition Fee (Semester 4)", amount_due=75000.0, amount_paid=75000.0, balance=0.0, due_date="2026-08-15", status="PAID"),
        FeeInvoice(invoice_number="INV-2026-8802", student_id="STU-2026-001", student_name="Aarav Patel", description="Hostel & Mess Fee - Term 1", amount_due=35000.0, amount_paid=35000.0, balance=0.0, due_date="2026-08-20", status="PAID"),
        FeeInvoice(invoice_number="INV-2026-8803", student_id="STU-2026-002", student_name="Diya Rao", description="Academic Year 2026-27 Tuition Fee (Semester 4)", amount_due=75000.0, amount_paid=50000.0, balance=25000.0, due_date="2026-09-15", status="PARTIALLY_PAID"),
    ]
