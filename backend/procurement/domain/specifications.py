"""
Procurement Management — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for procurement.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.procurement.domain.entities import ProcurementEntity

class ProcurementSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: ProcurementEntity) -> bool:
        pass

    def and_spec(self, other: "ProcurementSpecification") -> "ProcurementSpecification":
        return AndProcurementSpecification(self, other)

    def or_spec(self, other: "ProcurementSpecification") -> "ProcurementSpecification":
        return OrProcurementSpecification(self, other)

    def not_spec(self) -> "ProcurementSpecification":
        return NotProcurementSpecification(self)

class ActiveProcurementSpecification(ProcurementSpecification):
    def is_satisfied_by(self, candidate: ProcurementEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingProcurementSpecification(ProcurementSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: ProcurementEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndProcurementSpecification(ProcurementSpecification):
    def __init__(self, spec1: ProcurementSpecification, spec2: ProcurementSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ProcurementEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrProcurementSpecification(ProcurementSpecification):
    def __init__(self, spec1: ProcurementSpecification, spec2: ProcurementSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ProcurementEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotProcurementSpecification(ProcurementSpecification):
    def __init__(self, spec: ProcurementSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: ProcurementEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
