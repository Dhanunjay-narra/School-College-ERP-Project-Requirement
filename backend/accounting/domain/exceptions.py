"""
Accounts Payable & Receivable — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class AccountingNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Accounting entity with identifier '{entity_id}' was not found.")

class AccountingDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Accounting with unique code '{code}' already exists in tenant context.")

class AccountingInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Accounting is in '{current_state}' state.")
