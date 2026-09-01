"""
LMS & Assignments — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for assignments.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.assignments.domain.entities import AssignmentsEntity

class AssignmentsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: AssignmentsEntity) -> bool:
        pass

    def and_spec(self, other: "AssignmentsSpecification") -> "AssignmentsSpecification":
        return AndAssignmentsSpecification(self, other)

    def or_spec(self, other: "AssignmentsSpecification") -> "AssignmentsSpecification":
        return OrAssignmentsSpecification(self, other)

    def not_spec(self) -> "AssignmentsSpecification":
        return NotAssignmentsSpecification(self)

class ActiveAssignmentsSpecification(AssignmentsSpecification):
    def is_satisfied_by(self, candidate: AssignmentsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingAssignmentsSpecification(AssignmentsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: AssignmentsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndAssignmentsSpecification(AssignmentsSpecification):
    def __init__(self, spec1: AssignmentsSpecification, spec2: AssignmentsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AssignmentsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrAssignmentsSpecification(AssignmentsSpecification):
    def __init__(self, spec1: AssignmentsSpecification, spec2: AssignmentsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AssignmentsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotAssignmentsSpecification(AssignmentsSpecification):
    def __init__(self, spec: AssignmentsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: AssignmentsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
