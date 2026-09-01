"""
Parent & Guardian Management — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class ParentsDocSpec:
    """OpenAPI documentation and reference fixtures for Parent & Guardian Management."""

    SUMMARY = "Parent & Guardian Management API endpoint group for academic and institutional operations."
    TAGS = ["Parent & Guardian Management"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "PARE-2026-001",
                "name": "Standard Parent & Guardian Management Operational Record",
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
                "id": "PARE-UUID-8842",
                "tenant_id": "default_institution",
                "code": "PARE-2026-001",
                "name": "Standard Parent & Guardian Management Operational Record",
                "status": "ACTIVE"
            }
        }
