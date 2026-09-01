"""
Examinations & Grading — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for examinations.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.examinations.domain.entities import ExaminationsEntity

class ExaminationsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: ExaminationsEntity) -> bool:
        pass

    def and_spec(self, other: "ExaminationsSpecification") -> "ExaminationsSpecification":
        return AndExaminationsSpecification(self, other)

    def or_spec(self, other: "ExaminationsSpecification") -> "ExaminationsSpecification":
        return OrExaminationsSpecification(self, other)

    def not_spec(self) -> "ExaminationsSpecification":
        return NotExaminationsSpecification(self)

class ActiveExaminationsSpecification(ExaminationsSpecification):
    def is_satisfied_by(self, candidate: ExaminationsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingExaminationsSpecification(ExaminationsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: ExaminationsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndExaminationsSpecification(ExaminationsSpecification):
    def __init__(self, spec1: ExaminationsSpecification, spec2: ExaminationsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ExaminationsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrExaminationsSpecification(ExaminationsSpecification):
    def __init__(self, spec1: ExaminationsSpecification, spec2: ExaminationsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ExaminationsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotExaminationsSpecification(ExaminationsSpecification):
    def __init__(self, spec: ExaminationsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: ExaminationsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
