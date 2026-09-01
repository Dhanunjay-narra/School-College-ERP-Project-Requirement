"""
Organization & Multi-Campus — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for organization.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.organization.domain.entities import OrganizationEntity

class OrganizationSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: OrganizationEntity) -> bool:
        pass

    def and_spec(self, other: "OrganizationSpecification") -> "OrganizationSpecification":
        return AndOrganizationSpecification(self, other)

    def or_spec(self, other: "OrganizationSpecification") -> "OrganizationSpecification":
        return OrOrganizationSpecification(self, other)

    def not_spec(self) -> "OrganizationSpecification":
        return NotOrganizationSpecification(self)

class ActiveOrganizationSpecification(OrganizationSpecification):
    def is_satisfied_by(self, candidate: OrganizationEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingOrganizationSpecification(OrganizationSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: OrganizationEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndOrganizationSpecification(OrganizationSpecification):
    def __init__(self, spec1: OrganizationSpecification, spec2: OrganizationSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: OrganizationEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrOrganizationSpecification(OrganizationSpecification):
    def __init__(self, spec1: OrganizationSpecification, spec2: OrganizationSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: OrganizationEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotOrganizationSpecification(OrganizationSpecification):
    def __init__(self, spec: OrganizationSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: OrganizationEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
