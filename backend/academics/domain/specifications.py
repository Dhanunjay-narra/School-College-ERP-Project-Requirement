"""
Academic Structure & Timetable — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for academics.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.academics.domain.entities import AcademicsEntity

class AcademicsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: AcademicsEntity) -> bool:
        pass

    def and_spec(self, other: "AcademicsSpecification") -> "AcademicsSpecification":
        return AndAcademicsSpecification(self, other)

    def or_spec(self, other: "AcademicsSpecification") -> "AcademicsSpecification":
        return OrAcademicsSpecification(self, other)

    def not_spec(self) -> "AcademicsSpecification":
        return NotAcademicsSpecification(self)

class ActiveAcademicsSpecification(AcademicsSpecification):
    def is_satisfied_by(self, candidate: AcademicsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingAcademicsSpecification(AcademicsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: AcademicsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndAcademicsSpecification(AcademicsSpecification):
    def __init__(self, spec1: AcademicsSpecification, spec2: AcademicsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AcademicsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrAcademicsSpecification(AcademicsSpecification):
    def __init__(self, spec1: AcademicsSpecification, spec2: AcademicsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AcademicsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotAcademicsSpecification(AcademicsSpecification):
    def __init__(self, spec: AcademicsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: AcademicsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
