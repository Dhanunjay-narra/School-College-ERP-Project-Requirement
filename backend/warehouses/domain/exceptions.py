"""
Multi-Store Warehouse Management — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class WarehousesNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Warehouses entity with identifier '{entity_id}' was not found.")

class WarehousesDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Warehouses with unique code '{code}' already exists in tenant context.")

class WarehousesInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Warehouses is in '{current_state}' state.")
