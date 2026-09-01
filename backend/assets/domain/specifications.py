"""
Asset Lifecycle & Depreciation — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for assets.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.assets.domain.entities import AssetsEntity

class AssetsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: AssetsEntity) -> bool:
        pass

    def and_spec(self, other: "AssetsSpecification") -> "AssetsSpecification":
        return AndAssetsSpecification(self, other)

    def or_spec(self, other: "AssetsSpecification") -> "AssetsSpecification":
        return OrAssetsSpecification(self, other)

    def not_spec(self) -> "AssetsSpecification":
        return NotAssetsSpecification(self)

class ActiveAssetsSpecification(AssetsSpecification):
    def is_satisfied_by(self, candidate: AssetsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingAssetsSpecification(AssetsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: AssetsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndAssetsSpecification(AssetsSpecification):
    def __init__(self, spec1: AssetsSpecification, spec2: AssetsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AssetsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrAssetsSpecification(AssetsSpecification):
    def __init__(self, spec1: AssetsSpecification, spec2: AssetsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AssetsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotAssetsSpecification(AssetsSpecification):
    def __init__(self, spec: AssetsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: AssetsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
