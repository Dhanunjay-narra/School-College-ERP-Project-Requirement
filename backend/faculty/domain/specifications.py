"""
Faculty & Workload Management — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for faculty.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.faculty.domain.entities import FacultyEntity

class FacultySpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: FacultyEntity) -> bool:
        pass

    def and_spec(self, other: "FacultySpecification") -> "FacultySpecification":
        return AndFacultySpecification(self, other)

    def or_spec(self, other: "FacultySpecification") -> "FacultySpecification":
        return OrFacultySpecification(self, other)

    def not_spec(self) -> "FacultySpecification":
        return NotFacultySpecification(self)

class ActiveFacultySpecification(FacultySpecification):
    def is_satisfied_by(self, candidate: FacultyEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingFacultySpecification(FacultySpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: FacultyEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndFacultySpecification(FacultySpecification):
    def __init__(self, spec1: FacultySpecification, spec2: FacultySpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: FacultyEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrFacultySpecification(FacultySpecification):
    def __init__(self, spec1: FacultySpecification, spec2: FacultySpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: FacultyEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotFacultySpecification(FacultySpecification):
    def __init__(self, spec: FacultySpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: FacultyEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
