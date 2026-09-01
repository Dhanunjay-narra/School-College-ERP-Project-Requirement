"""
Identity & Access Management — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for identity.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.identity.domain.entities import IdentityEntity

class IdentitySpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: IdentityEntity) -> bool:
        pass

    def and_spec(self, other: "IdentitySpecification") -> "IdentitySpecification":
        return AndIdentitySpecification(self, other)

    def or_spec(self, other: "IdentitySpecification") -> "IdentitySpecification":
        return OrIdentitySpecification(self, other)

    def not_spec(self) -> "IdentitySpecification":
        return NotIdentitySpecification(self)

class ActiveIdentitySpecification(IdentitySpecification):
    def is_satisfied_by(self, candidate: IdentityEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingIdentitySpecification(IdentitySpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: IdentityEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndIdentitySpecification(IdentitySpecification):
    def __init__(self, spec1: IdentitySpecification, spec2: IdentitySpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: IdentityEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrIdentitySpecification(IdentitySpecification):
    def __init__(self, spec1: IdentitySpecification, spec2: IdentitySpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: IdentityEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotIdentitySpecification(IdentitySpecification):
    def __init__(self, spec: IdentitySpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: IdentityEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
