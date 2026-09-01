"""
Campus Infrastructure Projects — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class ProjectsDocSpec:
    """OpenAPI documentation and reference fixtures for Campus Infrastructure Projects."""

    SUMMARY = "Campus Infrastructure Projects API endpoint group for academic and institutional operations."
    TAGS = ["Campus Infrastructure Projects"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "PROJ-2026-001",
                "name": "Standard Campus Infrastructure Projects Operational Record",
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
                "id": "PROJ-UUID-8842",
                "tenant_id": "default_institution",
                "code": "PROJ-2026-001",
                "name": "Standard Campus Infrastructure Projects Operational Record",
                "status": "ACTIVE"
            }
        }
