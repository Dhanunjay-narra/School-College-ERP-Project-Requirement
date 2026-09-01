"""
Universal Enterprise Reporting — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class ReportingNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Reporting entity with identifier '{entity_id}' was not found.")

class ReportingDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Reporting with unique code '{code}' already exists in tenant context.")

class ReportingInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Reporting is in '{current_state}' state.")
