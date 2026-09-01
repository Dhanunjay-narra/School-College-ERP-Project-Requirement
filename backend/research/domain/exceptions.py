"""
Research & Innovation Management — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class ResearchNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Research entity with identifier '{entity_id}' was not found.")

class ResearchDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Research with unique code '{code}' already exists in tenant context.")

class ResearchInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Research is in '{current_state}' state.")
