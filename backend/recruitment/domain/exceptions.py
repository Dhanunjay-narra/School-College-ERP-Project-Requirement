"""
Applicant Tracking System — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class RecruitmentNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Recruitment entity with identifier '{entity_id}' was not found.")

class RecruitmentDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Recruitment with unique code '{code}' already exists in tenant context.")

class RecruitmentInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Recruitment is in '{current_state}' state.")
