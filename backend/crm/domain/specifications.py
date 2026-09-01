"""
Institutional CRM & Admissions Leads — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for crm.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.crm.domain.entities import CrmEntity

class CrmSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: CrmEntity) -> bool:
        pass

    def and_spec(self, other: "CrmSpecification") -> "CrmSpecification":
        return AndCrmSpecification(self, other)

    def or_spec(self, other: "CrmSpecification") -> "CrmSpecification":
        return OrCrmSpecification(self, other)

    def not_spec(self) -> "CrmSpecification":
        return NotCrmSpecification(self)

class ActiveCrmSpecification(CrmSpecification):
    def is_satisfied_by(self, candidate: CrmEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingCrmSpecification(CrmSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: CrmEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndCrmSpecification(CrmSpecification):
    def __init__(self, spec1: CrmSpecification, spec2: CrmSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: CrmEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrCrmSpecification(CrmSpecification):
    def __init__(self, spec1: CrmSpecification, spec2: CrmSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: CrmEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotCrmSpecification(CrmSpecification):
    def __init__(self, spec: CrmSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: CrmEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
