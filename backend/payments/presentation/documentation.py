"""
Payment Abstraction Gateway — OpenAPI Specifications & Mock Data Generators.
"""
from typing import Dict, Any, List

class PaymentsDocSpec:
    """OpenAPI documentation and reference fixtures for Payment Abstraction Gateway."""

    SUMMARY = "Payment Abstraction Gateway API endpoint group for academic and institutional operations."
    TAGS = ["Payment Abstraction Gateway"]

    @staticmethod
    def get_sample_request_fixture() -> Dict[str, Any]:
        return {
            "action": "CREATE_RECORD",
            "payload": {
                "code": "PAYM-2026-001",
                "name": "Standard Payment Abstraction Gateway Operational Record",
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
                "id": "PAYM-UUID-8842",
                "tenant_id": "default_institution",
                "code": "PAYM-2026-001",
                "name": "Standard Payment Abstraction Gateway Operational Record",
                "status": "ACTIVE"
            }
        }
