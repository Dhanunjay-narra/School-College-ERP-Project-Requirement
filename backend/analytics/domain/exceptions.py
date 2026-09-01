"""
BI & Institutional Analytics — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class AnalyticsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Analytics entity with identifier '{entity_id}' was not found.")

class AnalyticsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Analytics with unique code '{code}' already exists in tenant context.")

class AnalyticsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Analytics is in '{current_state}' state.")
