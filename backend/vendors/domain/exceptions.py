"""
Vendor Management & Compliance — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class VendorsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Vendors entity with identifier '{entity_id}' was not found.")

class VendorsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Vendors with unique code '{code}' already exists in tenant context.")

class VendorsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Vendors is in '{current_state}' state.")
