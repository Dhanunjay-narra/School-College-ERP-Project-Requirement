"""
Smart Attendance Engine — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class AttendanceDocSpec:
    """OpenAPI documentation and reference fixtures for Smart Attendance Engine."""

    SUMMARY = "Smart Attendance Engine API endpoint group for academic and institutional operations."
    TAGS = ["Smart Attendance Engine"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "ATTE-2026-001",
                "name": "Standard Smart Attendance Engine Operational Record",
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
                "id": "ATTE-UUID-8842",
                "tenant_id": "default_institution",
                "code": "ATTE-2026-001",
                "name": "Standard Smart Attendance Engine Operational Record",
                "status": "ACTIVE"
            }
        }
