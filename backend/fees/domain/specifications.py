"""
Fees & Student Billing — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for fees.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.fees.domain.entities import FeesEntity

class FeesSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: FeesEntity) -> bool:
        pass

    def and_spec(self, other: "FeesSpecification") -> "FeesSpecification":
        return AndFeesSpecification(self, other)

    def or_spec(self, other: "FeesSpecification") -> "FeesSpecification":
        return OrFeesSpecification(self, other)

    def not_spec(self) -> "FeesSpecification":
        return NotFeesSpecification(self)

class ActiveFeesSpecification(FeesSpecification):
    def is_satisfied_by(self, candidate: FeesEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingFeesSpecification(FeesSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: FeesEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndFeesSpecification(FeesSpecification):
    def __init__(self, spec1: FeesSpecification, spec2: FeesSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: FeesEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrFeesSpecification(FeesSpecification):
    def __init__(self, spec1: FeesSpecification, spec2: FeesSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: FeesEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotFeesSpecification(FeesSpecification):
    def __init__(self, spec: FeesSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: FeesEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
