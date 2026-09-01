"""
Campus Infrastructure Projects — Domain Business Rules & Invariant Validation Service.
"""
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from backend.projects.domain.entities import ProjectsEntity
from backend.core.exceptions import DomainException, ValidationException

logger = logging.getLogger("erp.projects.domain_service")

class ProjectsDomainService:
    """Encapsulates pure business logic and invariant checks for Campus Infrastructure Projects."""

    @staticmethod
    def validate_code_format(code: str) -> bool:
        """Validate standard uppercase alphanumeric format with hyphens."""
        if not code or len(code) < 2 or len(code) > 64:
            raise ValidationException("Code must be between 2 and 64 characters in length.")
        if not code.replace("-", "").isalnum():
            raise ValidationException("Code must contain only alphanumeric characters and hyphens.")
        return True

    @staticmethod
    def assert_valid_state_transition(current_status: str, new_status: str):
        """State machine invariant validation for projects."""
        valid_transitions = {
            "DRAFT": ["PENDING_REVIEW", "ACTIVE", "ARCHIVED"],
            "PENDING_REVIEW": ["APPROVED", "REJECTED", "ACTIVE"],
            "APPROVED": ["ACTIVE", "SUSPENDED", "COMPLETED"],
            "ACTIVE": ["SUSPENDED", "INACTIVE", "ARCHIVED", "COMPLETED"],
            "SUSPENDED": ["ACTIVE", "TERMINATED", "ARCHIVED"],
            "INACTIVE": ["ACTIVE", "ARCHIVED"],
            "COMPLETED": ["ARCHIVED"],
            "ARCHIVED": []
        }
        allowed = valid_transitions.get(current_status.upper(), ["ACTIVE", "INACTIVE", "ARCHIVED"])
        if new_status.upper() not in allowed and current_status.upper() != new_status.upper():
            raise DomainException(f"Invalid state transition from '{current_status}' to '{new_status}'.")

    @staticmethod
    def calculate_operational_health_score(entity: ProjectsEntity) -> float:
        """Calculate dynamic health and operational readiness score (0.0 - 100.0)."""
        score = 100.0
        if entity.status == "SUSPENDED":
            score -= 40.0
        elif entity.status == "INACTIVE":
            score -= 60.0
        elif entity.status == "ARCHIVED":
            score -= 90.0
        return max(0.0, score)
