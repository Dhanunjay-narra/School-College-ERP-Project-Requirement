"""
Academic Structure & Timetable — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class AcademicsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Academics entity with identifier '{entity_id}' was not found.")

class AcademicsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Academics with unique code '{code}' already exists in tenant context.")

class AcademicsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Academics is in '{current_state}' state.")
