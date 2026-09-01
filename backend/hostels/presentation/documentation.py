"""
Hostel & Housing Management — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class HostelsDocSpec:
    """OpenAPI documentation and reference fixtures for Hostel & Housing Management."""

    SUMMARY = "Hostel & Housing Management API endpoint group for academic and institutional operations."
    TAGS = ["Hostel & Housing Management"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "HOST-2026-001",
                "name": "Standard Hostel & Housing Management Operational Record",
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
                "id": "HOST-UUID-8842",
                "tenant_id": "default_institution",
                "code": "HOST-2026-001",
                "name": "Standard Hostel & Housing Management Operational Record",
                "status": "ACTIVE"
            }
        }
