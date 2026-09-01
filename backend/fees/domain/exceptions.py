"""
Fees & Student Billing — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class FeesNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Fees entity with identifier '{entity_id}' was not found.")

class FeesDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Fees with unique code '{code}' already exists in tenant context.")

class FeesInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Fees is in '{current_state}' state.")
