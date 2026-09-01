"""
Immutable Audit Logging — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class AuditNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Audit entity with identifier '{entity_id}' was not found.")

class AuditDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Audit with unique code '{code}' already exists in tenant context.")

class AuditInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Audit is in '{current_state}' state.")
