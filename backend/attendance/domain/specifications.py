"""
Smart Attendance Engine — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for attendance.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.attendance.domain.entities import AttendanceEntity

class AttendanceSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: AttendanceEntity) -> bool:
        pass

    def and_spec(self, other: "AttendanceSpecification") -> "AttendanceSpecification":
        return AndAttendanceSpecification(self, other)

    def or_spec(self, other: "AttendanceSpecification") -> "AttendanceSpecification":
        return OrAttendanceSpecification(self, other)

    def not_spec(self) -> "AttendanceSpecification":
        return NotAttendanceSpecification(self)

class ActiveAttendanceSpecification(AttendanceSpecification):
    def is_satisfied_by(self, candidate: AttendanceEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingAttendanceSpecification(AttendanceSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: AttendanceEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndAttendanceSpecification(AttendanceSpecification):
    def __init__(self, spec1: AttendanceSpecification, spec2: AttendanceSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AttendanceEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrAttendanceSpecification(AttendanceSpecification):
    def __init__(self, spec1: AttendanceSpecification, spec2: AttendanceSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AttendanceEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotAttendanceSpecification(AttendanceSpecification):
    def __init__(self, spec: AttendanceSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: AttendanceEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
