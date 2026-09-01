"""
Fees & Student Billing — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class FeesDocSpec:
    """OpenAPI documentation and reference fixtures for Fees & Student Billing."""

    SUMMARY = "Fees & Student Billing API endpoint group for academic and institutional operations."
    TAGS = ["Fees & Student Billing"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "FEES-2026-001",
                "name": "Standard Fees & Student Billing Operational Record",
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
                "id": "FEES-UUID-8842",
                "tenant_id": "default_institution",
                "code": "FEES-2026-001",
                "name": "Standard Fees & Student Billing Operational Record",
                "status": "ACTIVE"
            }
        }
