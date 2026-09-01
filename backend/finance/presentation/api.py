"""
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
