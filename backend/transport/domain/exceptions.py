"""
Transportation & GPS Fleet — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class TransportNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Transport entity with identifier '{entity_id}' was not found.")

class TransportDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Transport with unique code '{code}' already exists in tenant context.")

class TransportInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Transport is in '{current_state}' state.")
