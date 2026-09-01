"""
Universal Multi-Channel Notifications — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class CommunicationNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Communication entity with identifier '{entity_id}' was not found.")

class CommunicationDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Communication with unique code '{code}' already exists in tenant context.")

class CommunicationInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Communication is in '{current_state}' state.")
