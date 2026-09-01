"""
Student Information & Lifecycle — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for students.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.students.domain.entities import StudentsEntity

class StudentsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: StudentsEntity) -> bool:
        pass

    def and_spec(self, other: "StudentsSpecification") -> "StudentsSpecification":
        return AndStudentsSpecification(self, other)

    def or_spec(self, other: "StudentsSpecification") -> "StudentsSpecification":
        return OrStudentsSpecification(self, other)

    def not_spec(self) -> "StudentsSpecification":
        return NotStudentsSpecification(self)

class ActiveStudentsSpecification(StudentsSpecification):
    def is_satisfied_by(self, candidate: StudentsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingStudentsSpecification(StudentsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: StudentsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndStudentsSpecification(StudentsSpecification):
    def __init__(self, spec1: StudentsSpecification, spec2: StudentsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: StudentsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrStudentsSpecification(StudentsSpecification):
    def __init__(self, spec1: StudentsSpecification, spec2: StudentsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: StudentsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotStudentsSpecification(StudentsSpecification):
    def __init__(self, spec: StudentsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: StudentsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
