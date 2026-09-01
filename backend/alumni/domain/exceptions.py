"""
Alumni Network & Relations — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class AlumniNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Alumni entity with identifier '{entity_id}' was not found.")

class AlumniDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Alumni with unique code '{code}' already exists in tenant context.")

class AlumniInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Alumni is in '{current_state}' state.")
