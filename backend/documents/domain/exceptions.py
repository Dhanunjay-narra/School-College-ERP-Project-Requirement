"""
Document Management & Signatures — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class DocumentsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Documents entity with identifier '{entity_id}' was not found.")

class DocumentsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Documents with unique code '{code}' already exists in tenant context.")

class DocumentsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Documents is in '{current_state}' state.")
