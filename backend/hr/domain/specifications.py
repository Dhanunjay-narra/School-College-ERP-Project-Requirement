"""
Human Resource & Recruitment — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for hr.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.hr.domain.entities import HrEntity

class HrSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: HrEntity) -> bool:
        pass

    def and_spec(self, other: "HrSpecification") -> "HrSpecification":
        return AndHrSpecification(self, other)

    def or_spec(self, other: "HrSpecification") -> "HrSpecification":
        return OrHrSpecification(self, other)

    def not_spec(self) -> "HrSpecification":
        return NotHrSpecification(self)

class ActiveHrSpecification(HrSpecification):
    def is_satisfied_by(self, candidate: HrEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingHrSpecification(HrSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: HrEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndHrSpecification(HrSpecification):
    def __init__(self, spec1: HrSpecification, spec2: HrSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: HrEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrHrSpecification(HrSpecification):
    def __init__(self, spec1: HrSpecification, spec2: HrSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: HrEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotHrSpecification(HrSpecification):
    def __init__(self, spec: HrSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: HrEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
