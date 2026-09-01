"""
Configurable Workflow Engine — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class WorkflowsNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Workflows entity with identifier '{entity_id}' was not found.")

class WorkflowsDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Workflows with unique code '{code}' already exists in tenant context.")

class WorkflowsInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Workflows is in '{current_state}' state.")
