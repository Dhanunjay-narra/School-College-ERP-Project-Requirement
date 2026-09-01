"""
Campus Inventory & Stores — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class InventoryNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Inventory entity with identifier '{entity_id}' was not found.")

class InventoryDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Inventory with unique code '{code}' already exists in tenant context.")

class InventoryInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Inventory is in '{current_state}' state.")
