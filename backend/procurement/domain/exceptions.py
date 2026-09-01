"""
Procurement Management — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class ProcurementNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Procurement entity with identifier '{entity_id}' was not found.")

class ProcurementDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Procurement with unique code '{code}' already exists in tenant context.")

class ProcurementInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Procurement is in '{current_state}' state.")
