"""
BI & Institutional Analytics — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class AnalyticsDocSpec:
    """OpenAPI documentation and reference fixtures for BI & Institutional Analytics."""

    SUMMARY = "BI & Institutional Analytics API endpoint group for academic and institutional operations."
    TAGS = ["BI & Institutional Analytics"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "ANAL-2026-001",
                "name": "Standard BI & Institutional Analytics Operational Record",
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
                "id": "ANAL-UUID-8842",
                "tenant_id": "default_institution",
                "code": "ANAL-2026-001",
                "name": "Standard BI & Institutional Analytics Operational Record",
                "status": "ACTIVE"
            }
        }
