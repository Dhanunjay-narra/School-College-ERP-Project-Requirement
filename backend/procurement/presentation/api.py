"""
Procurement Management, RFQ, and Purchase Orders API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/procurement", tags=["Procurement & Vendor Management"])

class PurchaseOrder(BaseModel):
    po_number: str
    department: str
    vendor_name: str
    total_amount: float
    status: str
    created_date: str
    expected_delivery: str

@router.get("/purchase-orders", response_model=List[PurchaseOrder])
async def list_purchase_orders():
    return [
        PurchaseOrder(po_number="PO-2026-501", department="Computer Science", vendor_name="Dell Technologies India", total_amount=1850000.0, status="APPROVED_DELIVERED", created_date="2026-08-01", expected_delivery="2026-08-15"),
        PurchaseOrder(po_number="PO-2026-502", department="Mechanical Engineering", vendor_name="Kirloskar Machinery Ltd", total_amount=920000.0, status="IN_TRANSIT", created_date="2026-08-10", expected_delivery="2026-09-05"),
        PurchaseOrder(po_number="PO-2026-503", department="Central Library", vendor_name="Oxford University Press", total_amount=340000.0, status="RFQ_EVALUATED", created_date="2026-08-20", expected_delivery="2026-09-12"),
    ]
