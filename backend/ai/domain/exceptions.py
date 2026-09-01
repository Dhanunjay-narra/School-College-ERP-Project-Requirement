"""
AI/ML Predictive Intelligence — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class AiNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Ai entity with identifier '{entity_id}' was not found.")

class AiDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Ai with unique code '{code}' already exists in tenant context.")

class AiInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Ai is in '{current_state}' state.")
