"""
Identity & Access Management — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class IdentityNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Identity entity with identifier '{entity_id}' was not found.")

class IdentityDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Identity with unique code '{code}' already exists in tenant context.")

class IdentityInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Identity is in '{current_state}' state.")
