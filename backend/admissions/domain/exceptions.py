"""
Admissions CRM & Merit Engine — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class AdmissionsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Admissions entity with identifier '{entity_id}' was not found.")

class AdmissionsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Admissions with unique code '{code}' already exists in tenant context.")

class AdmissionsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Admissions is in '{current_state}' state.")
