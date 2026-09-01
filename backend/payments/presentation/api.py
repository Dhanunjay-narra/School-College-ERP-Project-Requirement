"""
Payment Abstraction Gateway API (UPI, Cards, NetBanking, Wallets, Cash/Cheques).
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/payments", tags=["Payment Abstraction Gateway"])

class PaymentTransaction(BaseModel):
    transaction_id: str
    invoice_number: str
    amount: float
    gateway_provider: str
    payment_method: str
    status: str
    timestamp: str

@router.get("/transactions", response_model=List[PaymentTransaction])
async def list_payment_transactions():
    return [
        PaymentTransaction(transaction_id="TXN-UPI-99210", invoice_number="INV-2026-8801", amount=75000.0, gateway_provider="UPI Adapter", payment_method="UPI / VPA", status="SUCCESS", timestamp="2026-08-12 14:32:00"),
        PaymentTransaction(transaction_id="TXN-CARD-99211", invoice_number="INV-2026-8802", amount=35000.0, gateway_provider="Card Adapter", payment_method="Credit Card", status="SUCCESS", timestamp="2026-08-18 11:15:22"),
        PaymentTransaction(transaction_id="TXN-CASH-99212", invoice_number="INV-2026-8803", amount=50000.0, gateway_provider="Cash / Counter Adapter", payment_method="Bank Deposit Receipt", status="SUCCESS", timestamp="2026-08-25 16:45:00"),
    ]
