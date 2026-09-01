"""
Campus Infrastructure Projects — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class ProjectsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Projects entity with identifier '{entity_id}' was not found.")

class ProjectsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Projects with unique code '{code}' already exists in tenant context.")

class ProjectsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Projects is in '{current_state}' state.")
