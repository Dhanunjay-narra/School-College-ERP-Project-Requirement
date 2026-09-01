"""
Campus Events & Conferences — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class EventsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Events entity with identifier '{entity_id}' was not found.")

class EventsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Events with unique code '{code}' already exists in tenant context.")

class EventsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Events is in '{current_state}' state.")
