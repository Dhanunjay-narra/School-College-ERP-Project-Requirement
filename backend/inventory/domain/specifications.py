"""
Campus Inventory & Stores — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for inventory.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.inventory.domain.entities import InventoryEntity

class InventorySpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: InventoryEntity) -> bool:
        pass

    def and_spec(self, other: "InventorySpecification") -> "InventorySpecification":
        return AndInventorySpecification(self, other)

    def or_spec(self, other: "InventorySpecification") -> "InventorySpecification":
        return OrInventorySpecification(self, other)

    def not_spec(self) -> "InventorySpecification":
        return NotInventorySpecification(self)

class ActiveInventorySpecification(InventorySpecification):
    def is_satisfied_by(self, candidate: InventoryEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingInventorySpecification(InventorySpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: InventoryEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndInventorySpecification(InventorySpecification):
    def __init__(self, spec1: InventorySpecification, spec2: InventorySpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: InventoryEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrInventorySpecification(InventorySpecification):
    def __init__(self, spec1: InventorySpecification, spec2: InventorySpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: InventoryEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotInventorySpecification(InventorySpecification):
    def __init__(self, spec: InventorySpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: InventoryEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
