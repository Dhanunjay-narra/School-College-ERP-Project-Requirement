"""
Finance & General Ledger — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for finance.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.finance.domain.entities import FinanceEntity

class FinanceSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: FinanceEntity) -> bool:
        pass

    def and_spec(self, other: "FinanceSpecification") -> "FinanceSpecification":
        return AndFinanceSpecification(self, other)

    def or_spec(self, other: "FinanceSpecification") -> "FinanceSpecification":
        return OrFinanceSpecification(self, other)

    def not_spec(self) -> "FinanceSpecification":
        return NotFinanceSpecification(self)

class ActiveFinanceSpecification(FinanceSpecification):
    def is_satisfied_by(self, candidate: FinanceEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingFinanceSpecification(FinanceSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: FinanceEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndFinanceSpecification(FinanceSpecification):
    def __init__(self, spec1: FinanceSpecification, spec2: FinanceSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: FinanceEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrFinanceSpecification(FinanceSpecification):
    def __init__(self, spec1: FinanceSpecification, spec2: FinanceSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: FinanceEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotFinanceSpecification(FinanceSpecification):
    def __init__(self, spec: FinanceSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: FinanceEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
