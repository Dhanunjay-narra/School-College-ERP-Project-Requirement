"""
Campus Workshop & Fab Lab — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for production.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.production.domain.entities import ProductionEntity

class ProductionSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: ProductionEntity) -> bool:
        pass

    def and_spec(self, other: "ProductionSpecification") -> "ProductionSpecification":
        return AndProductionSpecification(self, other)

    def or_spec(self, other: "ProductionSpecification") -> "ProductionSpecification":
        return OrProductionSpecification(self, other)

    def not_spec(self) -> "ProductionSpecification":
        return NotProductionSpecification(self)

class ActiveProductionSpecification(ProductionSpecification):
    def is_satisfied_by(self, candidate: ProductionEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingProductionSpecification(ProductionSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: ProductionEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndProductionSpecification(ProductionSpecification):
    def __init__(self, spec1: ProductionSpecification, spec2: ProductionSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ProductionEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrProductionSpecification(ProductionSpecification):
    def __init__(self, spec1: ProductionSpecification, spec2: ProductionSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ProductionEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotProductionSpecification(ProductionSpecification):
    def __init__(self, spec: ProductionSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: ProductionEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
