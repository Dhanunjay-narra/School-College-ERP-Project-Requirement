"""
Campus Store, Cafeteria POS, and Student Digital Wallet API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/campus-store", tags=["Campus Store & Cafeteria POS"])

class WalletBalance(BaseModel):
    student_id: str
    student_name: str
    wallet_balance: float
    last_recharge_date: str

class POSTransaction(BaseModel):
    receipt_id: str
    outlet: str
    items_count: int
    total_amount: float
    payment_mode: str
    timestamp: str

@router.get("/wallet", response_model=WalletBalance)
async def get_wallet():
    return WalletBalance(student_id="STU-2026-001", student_name="Aarav Patel", wallet_balance=2450.0, last_recharge_date="2026-08-28")

@router.get("/transactions", response_model=List[POSTransaction])
async def list_pos_transactions():
    return [
        POSTransaction(receipt_id="POS-REC-901", outlet="Aryabhata Cafeteria", items_count=2, total_amount=120.0, payment_mode="STUDENT_WALLET", timestamp="2026-08-31 12:45:00"),
        POSTransaction(receipt_id="POS-REC-902", outlet="Campus Stationery Store", items_count=3, total_amount=280.0, payment_mode="STUDENT_WALLET", timestamp="2026-08-30 16:10:00"),
    ]
