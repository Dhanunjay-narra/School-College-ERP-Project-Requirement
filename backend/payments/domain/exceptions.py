"""
Payment Abstraction Gateway — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class PaymentsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Payments entity with identifier '{entity_id}' was not found.")

class PaymentsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Payments with unique code '{code}' already exists in tenant context.")

class PaymentsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Payments is in '{current_state}' state.")
