"""
Vendor Management & Compliance — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class VendorsDocSpec:
    """OpenAPI documentation and reference fixtures for Vendor Management & Compliance."""

    SUMMARY = "Vendor Management & Compliance API endpoint group for academic and institutional operations."
    TAGS = ["Vendor Management & Compliance"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "VEND-2026-001",
                "name": "Standard Vendor Management & Compliance Operational Record",
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
                "id": "VEND-UUID-8842",
                "tenant_id": "default_institution",
                "code": "VEND-2026-001",
                "name": "Standard Vendor Management & Compliance Operational Record",
                "status": "ACTIVE"
            }
        }
