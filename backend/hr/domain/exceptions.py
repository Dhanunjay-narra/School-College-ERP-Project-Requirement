"""
Human Resource & Recruitment — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class HrNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Hr entity with identifier '{entity_id}' was not found.")

class HrDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Hr with unique code '{code}' already exists in tenant context.")

class HrInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Hr is in '{current_state}' state.")
