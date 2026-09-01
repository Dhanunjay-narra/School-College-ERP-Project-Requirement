"""
Test Operations, HR, Library, Transport, and AI Intelligence.
"""
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_list_employees():
    resp = client.get("/api/v1/hr/employees")
    assert resp.status_code == 200
    employees = resp.json()
    assert len(employees) >= 3

def test_list_books():
    resp = client.get("/api/v1/library/books")
    assert resp.status_code == 200
    books = resp.json()
    assert len(books) >= 3

def test_list_bus_routes():
    resp = client.get("/api/v1/transport/routes")
    assert resp.status_code == 200
    routes = resp.json()
    assert len(routes) >= 2

def test_ai_insights():
    resp = client.get("/api/v1/ai/insights")
    assert resp.status_code == 200
    insights = resp.json()
    assert len(insights) >= 3

def test_health_check():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "HEALTHY"
