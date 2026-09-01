"""
Integrated Payroll Engine — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for payroll.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.payroll.domain.entities import PayrollEntity

class PayrollSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: PayrollEntity) -> bool:
        pass

    def and_spec(self, other: "PayrollSpecification") -> "PayrollSpecification":
        return AndPayrollSpecification(self, other)

    def or_spec(self, other: "PayrollSpecification") -> "PayrollSpecification":
        return OrPayrollSpecification(self, other)

    def not_spec(self) -> "PayrollSpecification":
        return NotPayrollSpecification(self)

class ActivePayrollSpecification(PayrollSpecification):
    def is_satisfied_by(self, candidate: PayrollEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingPayrollSpecification(PayrollSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: PayrollEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndPayrollSpecification(PayrollSpecification):
    def __init__(self, spec1: PayrollSpecification, spec2: PayrollSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: PayrollEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrPayrollSpecification(PayrollSpecification):
    def __init__(self, spec1: PayrollSpecification, spec2: PayrollSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: PayrollEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotPayrollSpecification(PayrollSpecification):
    def __init__(self, spec: PayrollSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: PayrollEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
