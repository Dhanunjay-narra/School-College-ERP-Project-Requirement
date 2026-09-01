"""
Accreditation & Regulatory Compliance — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class ComplianceNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Compliance entity with identifier '{entity_id}' was not found.")

class ComplianceDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Compliance with unique code '{code}' already exists in tenant context.")

class ComplianceInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Compliance is in '{current_state}' state.")
