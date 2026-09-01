"""
Faculty & Workload Management — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class FacultyNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Faculty entity with identifier '{entity_id}' was not found.")

class FacultyDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Faculty with unique code '{code}' already exists in tenant context.")

class FacultyInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Faculty is in '{current_state}' state.")
