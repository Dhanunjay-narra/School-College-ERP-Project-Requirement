"""
Academic Structure & Timetable — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class AcademicsDocSpec:
    """OpenAPI documentation and reference fixtures for Academic Structure & Timetable."""

    SUMMARY = "Academic Structure & Timetable API endpoint group for academic and institutional operations."
    TAGS = ["Academic Structure & Timetable"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "ACAD-2026-001",
                "name": "Standard Academic Structure & Timetable Operational Record",
                "status": "ACTIVE",
                "department": "Computer Science & Engineering",
                "campus": "Main Academic Campus"
            },
            "client_version": "1.0.0"
        }

    @staticmethod
    def get_sample_response_fixture() -> Dict[str, Any]:
        return {
            "success": True,
            "status_code": 200,
            "message": "Resource processed successfully",
            "data": {
                "id": "ACAD-UUID-8842",
                "tenant_id": "default_institution",
                "code": "ACAD-2026-001",
                "name": "Standard Academic Structure & Timetable Operational Record",
                "status": "ACTIVE"
            }
        }
