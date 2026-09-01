"""
Identity Domain Value Objects.
"""
from enum import Enum
from dataclasses import dataclass
from typing import Optional
import re

class RoleType(str, Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    INSTITUTION_ADMIN = "INSTITUTION_ADMIN"
    CAMPUS_ADMIN = "CAMPUS_ADMIN"
    PRINCIPAL = "PRINCIPAL"
    DIRECTOR = "DIRECTOR"
    HOD = "HOD"
    FACULTY = "FACULTY"
    ACCOUNTANT = "ACCOUNTANT"
    HR_MANAGER = "HR_MANAGER"
    LIBRARIAN = "LIBRARIAN"
    TRANSPORT_MANAGER = "TRANSPORT_MANAGER"
    HOSTEL_WARDEN = "HOSTEL_WARDEN"
    EXAM_CONTROLLER = "EXAM_CONTROLLER"
    STUDENT = "STUDENT"
    PARENT = "PARENT"
    ALUMNI = "ALUMNI"
    VENDOR = "VENDOR"

class SessionStatus(str, Enum):
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"
    LOCKED = "LOCKED"

@dataclass(frozen=True)
class EmailAddress:
    value: str

    def __post_init__(self):
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, self.value):
            raise ValueError(f"Invalid email address: {self.value}")

    def __str__(self) -> str:
        return self.value.lower()
