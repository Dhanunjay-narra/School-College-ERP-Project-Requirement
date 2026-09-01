"""
Payment Abstraction Gateway — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for payments.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.payments.domain.entities import PaymentsEntity

class PaymentsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: PaymentsEntity) -> bool:
        pass

    def and_spec(self, other: "PaymentsSpecification") -> "PaymentsSpecification":
        return AndPaymentsSpecification(self, other)

    def or_spec(self, other: "PaymentsSpecification") -> "PaymentsSpecification":
        return OrPaymentsSpecification(self, other)

    def not_spec(self) -> "PaymentsSpecification":
        return NotPaymentsSpecification(self)

class ActivePaymentsSpecification(PaymentsSpecification):
    def is_satisfied_by(self, candidate: PaymentsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingPaymentsSpecification(PaymentsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: PaymentsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndPaymentsSpecification(PaymentsSpecification):
    def __init__(self, spec1: PaymentsSpecification, spec2: PaymentsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: PaymentsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrPaymentsSpecification(PaymentsSpecification):
    def __init__(self, spec1: PaymentsSpecification, spec2: PaymentsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: PaymentsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotPaymentsSpecification(PaymentsSpecification):
    def __init__(self, spec: PaymentsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: PaymentsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
