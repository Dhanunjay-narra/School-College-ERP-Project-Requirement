"""
Immutable Audit Logging — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for audit.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.audit.domain.entities import AuditEntity

class AuditSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: AuditEntity) -> bool:
        pass

    def and_spec(self, other: "AuditSpecification") -> "AuditSpecification":
        return AndAuditSpecification(self, other)

    def or_spec(self, other: "AuditSpecification") -> "AuditSpecification":
        return OrAuditSpecification(self, other)

    def not_spec(self) -> "AuditSpecification":
        return NotAuditSpecification(self)

class ActiveAuditSpecification(AuditSpecification):
    def is_satisfied_by(self, candidate: AuditEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingAuditSpecification(AuditSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: AuditEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndAuditSpecification(AuditSpecification):
    def __init__(self, spec1: AuditSpecification, spec2: AuditSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AuditEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrAuditSpecification(AuditSpecification):
    def __init__(self, spec1: AuditSpecification, spec2: AuditSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AuditEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotAuditSpecification(AuditSpecification):
    def __init__(self, spec: AuditSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: AuditEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
