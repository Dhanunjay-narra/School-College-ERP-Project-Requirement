"""
Multi-Store Warehouse Management — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for warehouses.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.warehouses.domain.entities import WarehousesEntity

class WarehousesSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: WarehousesEntity) -> bool:
        pass

    def and_spec(self, other: "WarehousesSpecification") -> "WarehousesSpecification":
        return AndWarehousesSpecification(self, other)

    def or_spec(self, other: "WarehousesSpecification") -> "WarehousesSpecification":
        return OrWarehousesSpecification(self, other)

    def not_spec(self) -> "WarehousesSpecification":
        return NotWarehousesSpecification(self)

class ActiveWarehousesSpecification(WarehousesSpecification):
    def is_satisfied_by(self, candidate: WarehousesEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingWarehousesSpecification(WarehousesSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: WarehousesEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndWarehousesSpecification(WarehousesSpecification):
    def __init__(self, spec1: WarehousesSpecification, spec2: WarehousesSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: WarehousesEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrWarehousesSpecification(WarehousesSpecification):
    def __init__(self, spec1: WarehousesSpecification, spec2: WarehousesSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: WarehousesEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotWarehousesSpecification(WarehousesSpecification):
    def __init__(self, spec: WarehousesSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: WarehousesEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
