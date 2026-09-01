"""
Integrated Payroll Engine — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class PayrollNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Payroll entity with identifier '{entity_id}' was not found.")

class PayrollDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Payroll with unique code '{code}' already exists in tenant context.")

class PayrollInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Payroll is in '{current_state}' state.")
