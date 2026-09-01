"""
Procurement Management — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class ProcurementDocSpec:
    """OpenAPI documentation and reference fixtures for Procurement Management."""

    SUMMARY = "Procurement Management API endpoint group for academic and institutional operations."
    TAGS = ["Procurement Management"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "PROC-2026-001",
                "name": "Standard Procurement Management Operational Record",
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
                "id": "PROC-UUID-8842",
                "tenant_id": "default_institution",
                "code": "PROC-2026-001",
                "name": "Standard Procurement Management Operational Record",
                "status": "ACTIVE"
            }
        }
