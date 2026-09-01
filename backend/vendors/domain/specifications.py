"""
Vendor Management & Compliance — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for vendors.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.vendors.domain.entities import VendorsEntity

class VendorsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: VendorsEntity) -> bool:
        pass

    def and_spec(self, other: "VendorsSpecification") -> "VendorsSpecification":
        return AndVendorsSpecification(self, other)

    def or_spec(self, other: "VendorsSpecification") -> "VendorsSpecification":
        return OrVendorsSpecification(self, other)

    def not_spec(self) -> "VendorsSpecification":
        return NotVendorsSpecification(self)

class ActiveVendorsSpecification(VendorsSpecification):
    def is_satisfied_by(self, candidate: VendorsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingVendorsSpecification(VendorsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: VendorsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndVendorsSpecification(VendorsSpecification):
    def __init__(self, spec1: VendorsSpecification, spec2: VendorsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: VendorsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrVendorsSpecification(VendorsSpecification):
    def __init__(self, spec1: VendorsSpecification, spec2: VendorsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: VendorsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotVendorsSpecification(VendorsSpecification):
    def __init__(self, spec: VendorsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: VendorsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
