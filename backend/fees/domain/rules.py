"""
Fees & Student Billing — Business Policy Rules & Constraints.
Defines domain policy specifications, operational invariants, and eligibility predicates for fees.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime
from backend.core.exceptions import DomainException, ValidationException

class FeesBusinessRules:
    """Domain rule evaluator for Fees & Student Billing."""

    @classmethod
    def evaluate_creation_policy(cls, data: Dict[str, Any], tenant_id: str) -> bool:
        """Validate institutional policy requirements prior to creation."""
        if not data.get("code"):
            raise ValidationException("Unique identifier code is strictly required by institutional policy.")
        if len(str(data.get("name", ""))) < 3:
            raise ValidationException("Entity name must contain at least 3 characters.")
        return True

    @classmethod
    def evaluate_modification_policy(cls, entity_id: str, updates: Dict[str, Any], user_roles: List[str]) -> bool:
        """Enforce permission rules for entity modifications."""
        privileged_roles = ["SUPER_ADMIN", "INSTITUTION_ADMIN", "PRINCIPAL", "HOD"]
        if not any(r in privileged_roles for r in user_roles):
            # Check standard domain updates
            if "status" in updates and updates["status"] in ["DELETED", "PURGED", "ARCHIVED"]:
                raise DomainException("Only authorized administrators can purge or archive operational records.")
        return True

    @classmethod
    def compute_risk_score(cls, entity_state: Dict[str, Any]) -> float:
        """Compute operational risk score (0.0 to 10.0) based on domain invariants."""
        risk = 1.0
        if entity_state.get("status") == "SUSPENDED":
            risk += 4.5
        elif entity_state.get("status") == "PENDING_REVIEW":
            risk += 2.0
        return min(10.0, risk)
