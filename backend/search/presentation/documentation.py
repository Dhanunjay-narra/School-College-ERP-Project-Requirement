"""
Centralized Faceted Search — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class SearchDocSpec:
    """OpenAPI documentation and reference fixtures for Centralized Faceted Search."""

    SUMMARY = "Centralized Faceted Search API endpoint group for academic and institutional operations."
    TAGS = ["Centralized Faceted Search"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "SEAR-2026-001",
                "name": "Standard Centralized Faceted Search Operational Record",
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
                "id": "SEAR-UUID-8842",
                "tenant_id": "default_institution",
                "code": "SEAR-2026-001",
                "name": "Standard Centralized Faceted Search Operational Record",
                "status": "ACTIVE"
            }
        }
