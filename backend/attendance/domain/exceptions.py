"""
Smart Attendance Engine — Domain-Specific Exception Definitions.
"""
from backend.core.exceptions import DomainException

class AttendanceNotFoundException(DomainException):
    def __init__(self, entity_id: str):
        super().__init__(f"Attendance entity with identifier '{entity_id}' was not found.")

class AttendanceDuplicateCodeException(DomainException):
    def __init__(self, code: str):
        super().__init__(f"Attendance with unique code '{code}' already exists in tenant context.")

class AttendanceInvalidStateException(DomainException):
    def __init__(self, current_state: str, attempted_action: str):
        super().__init__(f"Cannot perform '{attempted_action}' when Attendance is in '{current_state}' state.")
