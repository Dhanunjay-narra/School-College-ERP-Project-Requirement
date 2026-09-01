"""
Test Student & Academic Domains.
"""
import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_list_students():
    resp = client.get("/api/v1/students/")
    assert resp.status_code == 200
    students = resp.json()
    assert len(students) >= 2
    assert students[0]["roll_number"] == "24CSE042"

def test_list_courses():
    resp = client.get("/api/v1/academics/courses")
    assert resp.status_code == 200
    courses = resp.json()
    assert len(courses) >= 4
    assert courses[0]["code"] == "CS401"

def test_get_timetable():
    resp = client.get("/api/v1/academics/timetable")
    assert resp.status_code == 200
    slots = resp.json()
    assert len(slots) >= 4
