"""
Student Information & Lifecycle — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class StudentsDocSpec:
    """OpenAPI documentation and reference fixtures for Student Information & Lifecycle."""

    SUMMARY = "Student Information & Lifecycle API endpoint group for academic and institutional operations."
    TAGS = ["Student Information & Lifecycle"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "STUD-2026-001",
                "name": "Standard Student Information & Lifecycle Operational Record",
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
                "id": "STUD-UUID-8842",
                "tenant_id": "default_institution",
                "code": "STUD-2026-001",
                "name": "Standard Student Information & Lifecycle Operational Record",
                "status": "ACTIVE"
            }
        }
