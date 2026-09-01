"""
Institutional CRM & Admissions Leads — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class CrmNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Crm entity with identifier '{entity_id}' was not found.")

class CrmDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Crm with unique code '{code}' already exists in tenant context.")

class CrmInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Crm is in '{current_state}' state.")
