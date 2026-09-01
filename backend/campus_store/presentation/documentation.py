"""
Campus Store & Cafeteria POS — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class CampusStoreDocSpec:
    """OpenAPI documentation and reference fixtures for Campus Store & Cafeteria POS."""

    SUMMARY = "Campus Store & Cafeteria POS API endpoint group for academic and institutional operations."
    TAGS = ["Campus Store & Cafeteria POS"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "CAMP-2026-001",
                "name": "Standard Campus Store & Cafeteria POS Operational Record",
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
                "id": "CAMP-UUID-8842",
                "tenant_id": "default_institution",
                "code": "CAMP-2026-001",
                "name": "Standard Campus Store & Cafeteria POS Operational Record",
                "status": "ACTIVE"
            }
        }
