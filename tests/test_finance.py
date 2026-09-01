"""
Test Fees, Payments, Finance & Procurement Domains.
"""
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_list_fee_invoices():
    resp = client.get("/api/v1/fees/invoices")
    assert resp.status_code == 200
    invoices = resp.json()
    assert len(invoices) >= 3

def test_finance_summary():
    resp = client.get("/api/v1/finance/summary")
    assert resp.status_code == 200
    summary = resp.json()
    assert summary["total_revenue_ytd"] > 0

def test_list_purchase_orders():
    resp = client.get("/api/v1/procurement/purchase-orders")
    assert resp.status_code == 200
    pos = resp.json()
    assert len(pos) >= 3
