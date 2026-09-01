"""
Student Domain Value Objects.
"""
from enum import Enum

class StudentStatus(str, Enum):
    ENQUIRY = "ENQUIRY"
    APPLICANT = "APPLICANT"
    APPLICATION_SUBMITTED = "APPLICATION_SUBMITTED"
    SHORTLISTED = "SHORTLISTED"
    ADMITTED = "ADMITTED"
    ENROLLED = "ENROLLED"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    WITHDRAWN = "WITHDRAWN"
    TRANSFERRED = "TRANSFERRED"
    GRADUATED = "GRADUATED"
    ALUMNI = "ALUMNI"

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

class BloodGroup(str, Enum):
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"
