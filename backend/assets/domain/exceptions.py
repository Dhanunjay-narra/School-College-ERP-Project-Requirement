"""
Asset Lifecycle & Depreciation — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class AssetsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Assets entity with identifier '{entity_id}' was not found.")

class AssetsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Assets with unique code '{code}' already exists in tenant context.")

class AssetsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Assets is in '{current_state}' state.")
