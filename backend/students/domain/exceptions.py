"""
Student Information & Lifecycle — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class StudentsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Students entity with identifier '{entity_id}' was not found.")

class StudentsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Students with unique code '{code}' already exists in tenant context.")

class StudentsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Students is in '{current_state}' state.")
