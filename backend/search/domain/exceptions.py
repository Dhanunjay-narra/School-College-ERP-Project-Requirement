"""
Centralized Faceted Search — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class SearchNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Search entity with identifier '{entity_id}' was not found.")

class SearchDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Search with unique code '{code}' already exists in tenant context.")

class SearchInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Search is in '{current_state}' state.")
