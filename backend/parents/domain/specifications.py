"""
Parent & Guardian Management — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for parents.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.parents.domain.entities import ParentsEntity

class ParentsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: ParentsEntity) -> bool:
        pass

    def and_spec(self, other: "ParentsSpecification") -> "ParentsSpecification":
        return AndParentsSpecification(self, other)

    def or_spec(self, other: "ParentsSpecification") -> "ParentsSpecification":
        return OrParentsSpecification(self, other)

    def not_spec(self) -> "ParentsSpecification":
        return NotParentsSpecification(self)

class ActiveParentsSpecification(ParentsSpecification):
    def is_satisfied_by(self, candidate: ParentsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingParentsSpecification(ParentsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: ParentsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndParentsSpecification(ParentsSpecification):
    def __init__(self, spec1: ParentsSpecification, spec2: ParentsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ParentsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrParentsSpecification(ParentsSpecification):
    def __init__(self, spec1: ParentsSpecification, spec2: ParentsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ParentsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotParentsSpecification(ParentsSpecification):
    def __init__(self, spec: ParentsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: ParentsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
