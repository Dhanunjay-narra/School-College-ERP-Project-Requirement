"""
Campus Store & Cafeteria POS — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class CampusStoreNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"CampusStore entity with identifier '{entity_id}' was not found.")

class CampusStoreDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"CampusStore with unique code '{code}' already exists in tenant context.")

class CampusStoreInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when CampusStore is in '{current_state}' state.")
