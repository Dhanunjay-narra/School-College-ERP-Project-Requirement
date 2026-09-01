"""
Hostel & Housing Management — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class HostelsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Hostels entity with identifier '{entity_id}' was not found.")

class HostelsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Hostels with unique code '{code}' already exists in tenant context.")

class HostelsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Hostels is in '{current_state}' state.")
