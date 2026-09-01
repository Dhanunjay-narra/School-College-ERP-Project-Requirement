"""
Admissions CRM & Merit Engine — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class AdmissionsDocSpec:
    """OpenAPI documentation and reference fixtures for Admissions CRM & Merit Engine."""

    SUMMARY = "Admissions CRM & Merit Engine API endpoint group for academic and institutional operations."
    TAGS = ["Admissions CRM & Merit Engine"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "ADMI-2026-001",
                "name": "Standard Admissions CRM & Merit Engine Operational Record",
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
                "id": "ADMI-UUID-8842",
                "tenant_id": "default_institution",
                "code": "ADMI-2026-001",
                "name": "Standard Admissions CRM & Merit Engine Operational Record",
                "status": "ACTIVE"
            }
        }
