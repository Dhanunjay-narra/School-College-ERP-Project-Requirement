"""
Parent & Guardian Management — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class ParentsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Parents entity with identifier '{entity_id}' was not found.")

class ParentsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Parents with unique code '{code}' already exists in tenant context.")

class ParentsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Parents is in '{current_state}' state.")
