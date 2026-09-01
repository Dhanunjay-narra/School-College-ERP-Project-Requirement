"""
Transportation & GPS Fleet — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class TransportDocSpec:
    """OpenAPI documentation and reference fixtures for Transportation & GPS Fleet."""

    SUMMARY = "Transportation & GPS Fleet API endpoint group for academic and institutional operations."
    TAGS = ["Transportation & GPS Fleet"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "TRAN-2026-001",
                "name": "Standard Transportation & GPS Fleet Operational Record",
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
                "id": "TRAN-UUID-8842",
                "tenant_id": "default_institution",
                "code": "TRAN-2026-001",
                "name": "Standard Transportation & GPS Fleet Operational Record",
                "status": "ACTIVE"
            }
        }
