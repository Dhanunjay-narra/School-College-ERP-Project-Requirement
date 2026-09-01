"""
Examinations & Grading — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class ExaminationsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Examinations entity with identifier '{entity_id}' was not found.")

class ExaminationsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Examinations with unique code '{code}' already exists in tenant context.")

class ExaminationsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Examinations is in '{current_state}' state.")
