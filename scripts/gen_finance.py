from writer_util import write_f

def build_finance_domains():
    print("[PHASES 12-16, 28] Generating Finance, Procurement, Supply Chain & Campus Commerce...")

    # Phase 12: Fees & Billing
    write_f("backend/fees/__init__.py", "")
    write_f("backend/fees/presentation/api.py", '''"""
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
''')

    # Phase 13: Payments
    write_f("backend/payments/__init__.py", "")
    write_f("backend/payments/presentation/api.py", '''"""
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
''')

    # Phase 14: Finance & General Ledger
    write_f("backend/finance/__init__.py", "")
    write_f("backend/finance/presentation/api.py", '''"""
General Ledger, Chart of Accounts, and Financial Statements API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/finance", tags=["Finance & General Ledger"])

class AccountBalance(BaseModel):
    account_code: str
    account_name: str
    category: str
    debit: float
    credit: float
    net_balance: float

class FinancialSummary(BaseModel):
    total_revenue_ytd: float
    total_expenses_ytd: float
    net_operating_surplus: float
    cash_and_bank_balance: float
    outstanding_student_receivables: float

@router.get("/summary", response_model=FinancialSummary)
async def get_financial_summary():
    return FinancialSummary(
        total_revenue_ytd=128500000.0,
        total_expenses_ytd=84200000.0,
        net_operating_surplus=44300000.0,
        cash_and_bank_balance=62500000.0,
        outstanding_student_receivables=4200000.0
    )

@router.get("/chart-of-accounts", response_model=List[AccountBalance])
async def get_chart_of_accounts():
    return [
        AccountBalance(account_code="1010", account_name="Main Operating Bank Account", category="ASSET", debit=52000000.0, credit=0.0, net_balance=52000000.0),
        AccountBalance(account_code="1020", account_name="Petty Cash Reserve", category="ASSET", debit=500000.0, credit=0.0, net_balance=500000.0),
        AccountBalance(account_code="1200", account_name="Student Accounts Receivable", category="ASSET", debit=4200000.0, credit=0.0, net_balance=4200000.0),
        AccountBalance(account_code="4010", account_name="Tuition Fee Revenue", category="REVENUE", debit=0.0, credit=98000000.0, net_balance=98000000.0),
        AccountBalance(account_code="5010", account_name="Faculty & Staff Payroll Expense", category="EXPENSE", debit=48000000.0, credit=0.0, net_balance=48000000.0),
    ]
''')

    # Phase 15: Procurement & Vendors
    write_f("backend/procurement/__init__.py", "")
    write_f("backend/procurement/presentation/api.py", '''"""
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
''')

    # Phase 16: Campus Inventory & Warehouses
    write_f("backend/inventory/__init__.py", "")
    write_f("backend/inventory/presentation/api.py", '''"""
Campus Inventory & Multi-Store Warehouse API.
"""
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter(prefix="/inventory", tags=["Campus Inventory & Stores"])

class InventoryItem(BaseModel):
    sku: str
    item_name: str
    category: str
    store_location: str
    current_quantity: int
    reorder_level: int
    unit: str
    status: str

@router.get("/stock", response_model=List[InventoryItem])
async def list_inventory_stock():
    return [
        InventoryItem(sku="SKU-CS-LAB-01", item_name="Dell OptiPlex Core i7 Workstation", category="Computers & Hardware", store_location="Computer Store (ACB-002)", current_quantity=65, reorder_level=10, unit="Units", status="IN_STOCK"),
        InventoryItem(sku="SKU-CHE-LAB-12", item_name="Sodium Hydroxide Analytical Grade 500g", category="Laboratory Consumables", store_location="Science Store (SC-101)", current_quantity=24, reorder_level=5, unit="Bottles", status="IN_STOCK"),
        InventoryItem(sku="SKU-STAT-004", item_name="A4 Examination Answer Booklets (32-Page)", category="Stationery & Printing", store_location="Central Store (ADM-010)", current_quantity=12000, reorder_level=2000, unit="Booklets", status="IN_STOCK"),
    ]
''')

    # Phase 28: Campus Store / POS & Canteen
    write_f("backend/campus_store/__init__.py", "")
    write_f("backend/campus_store/presentation/api.py", '''"""
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
''')

    print("[GEN] Finance, Procurement & Campus Commerce completed.")

if __name__ == '__main__':
    build_finance_domains()
