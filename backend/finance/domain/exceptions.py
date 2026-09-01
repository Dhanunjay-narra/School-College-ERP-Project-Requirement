"""
Finance & General Ledger — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class FinanceNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Finance entity with identifier '{entity_id}' was not found.")

class FinanceDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Finance with unique code '{code}' already exists in tenant context.")

class FinanceInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Finance is in '{current_state}' state.")
