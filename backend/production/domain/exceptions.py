"""
Campus Workshop & Fab Lab — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class ProductionNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Production entity with identifier '{entity_id}' was not found.")

class ProductionDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Production with unique code '{code}' already exists in tenant context.")

class ProductionInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Production is in '{current_state}' state.")
