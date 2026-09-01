"""
LMS & Assignments — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class AssignmentsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Assignments entity with identifier '{entity_id}' was not found.")

class AssignmentsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Assignments with unique code '{code}' already exists in tenant context.")

class AssignmentsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Assignments is in '{current_state}' state.")
