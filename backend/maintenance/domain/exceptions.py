"""
Campus Facility Maintenance — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class MaintenanceNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Maintenance entity with identifier '{entity_id}' was not found.")

class MaintenanceDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Maintenance with unique code '{code}' already exists in tenant context.")

class MaintenanceInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Maintenance is in '{current_state}' state.")
