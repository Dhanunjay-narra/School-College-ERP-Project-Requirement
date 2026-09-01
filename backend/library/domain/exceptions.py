"""
Library & RFID Circulation — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class LibraryNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Library entity with identifier '{entity_id}' was not found.")

class LibraryDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Library with unique code '{code}' already exists in tenant context.")

class LibraryInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Library is in '{current_state}' state.")
