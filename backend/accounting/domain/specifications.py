"""
Accounts Payable & Receivable — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for accounting.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.accounting.domain.entities import AccountingEntity

class AccountingSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: AccountingEntity) -> bool:
        pass

    def and_spec(self, other: "AccountingSpecification") -> "AccountingSpecification":
        return AndAccountingSpecification(self, other)

    def or_spec(self, other: "AccountingSpecification") -> "AccountingSpecification":
        return OrAccountingSpecification(self, other)

    def not_spec(self) -> "AccountingSpecification":
        return NotAccountingSpecification(self)

class ActiveAccountingSpecification(AccountingSpecification):
    def is_satisfied_by(self, candidate: AccountingEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingAccountingSpecification(AccountingSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: AccountingEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndAccountingSpecification(AccountingSpecification):
    def __init__(self, spec1: AccountingSpecification, spec2: AccountingSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AccountingEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrAccountingSpecification(AccountingSpecification):
    def __init__(self, spec1: AccountingSpecification, spec2: AccountingSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AccountingEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotAccountingSpecification(AccountingSpecification):
    def __init__(self, spec: AccountingSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: AccountingEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
