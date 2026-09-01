"""
Test Organization & Multi-Campus Hierarchy.
"""
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_institution():
    resp = client.get("/api/v1/organization/institution")
    assert resp.status_code == 200
    data = resp.json()
    assert data["code"] == "AITM"
    assert data["institution_type"] == "UNIVERSITY"

def test_list_campuses():
    resp = client.get("/api/v1/organization/campuses")
    assert resp.status_code == 200
    campuses = resp.json()
    assert len(campuses) > 0
    assert campuses[0]["code"] == "MAIN"

def test_list_departments():
    resp = client.get("/api/v1/organization/departments")
    assert resp.status_code == 200
    depts = resp.json()
    assert any(d["code"] == "CSE" for d in depts)
