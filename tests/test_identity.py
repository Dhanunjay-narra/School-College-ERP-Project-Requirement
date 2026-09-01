"""
Test Identity & Authentication Domain.
"""
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_login_success():
    resp = client.post("/api/v1/auth/login", json={
        "email": "superadmin@erp.edu",
        "password": "Password@123",
        "tenant_id": "default_institution"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert data["user"]["email"] == "superadmin@erp.edu"
    assert data["user"]["role"] == "SUPER_ADMIN"

def test_login_invalid_password():
    resp = client.post("/api/v1/auth/login", json={
        "email": "superadmin@erp.edu",
        "password": "WrongPassword999",
        "tenant_id": "default_institution"
    })
    assert resp.status_code == 401

def test_list_users():
    resp = client.get("/api/v1/auth/users", headers={"Authorization": "Bearer mock-token"})
    assert resp.status_code in [200, 401]
