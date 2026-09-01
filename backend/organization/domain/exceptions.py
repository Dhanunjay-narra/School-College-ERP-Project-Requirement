"""
Organization & Multi-Campus — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class OrganizationNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Organization entity with identifier '{entity_id}' was not found.")

class OrganizationDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Organization with unique code '{code}' already exists in tenant context.")

class OrganizationInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Organization is in '{current_state}' state.")
