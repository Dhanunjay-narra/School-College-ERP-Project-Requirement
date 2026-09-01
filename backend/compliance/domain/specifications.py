"""
Accreditation & Regulatory Compliance — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for compliance.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.compliance.domain.entities import ComplianceEntity

class ComplianceSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: ComplianceEntity) -> bool:
        pass

    def and_spec(self, other: "ComplianceSpecification") -> "ComplianceSpecification":
        return AndComplianceSpecification(self, other)

    def or_spec(self, other: "ComplianceSpecification") -> "ComplianceSpecification":
        return OrComplianceSpecification(self, other)

    def not_spec(self) -> "ComplianceSpecification":
        return NotComplianceSpecification(self)

class ActiveComplianceSpecification(ComplianceSpecification):
    def is_satisfied_by(self, candidate: ComplianceEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingComplianceSpecification(ComplianceSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: ComplianceEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndComplianceSpecification(ComplianceSpecification):
    def __init__(self, spec1: ComplianceSpecification, spec2: ComplianceSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ComplianceEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrComplianceSpecification(ComplianceSpecification):
    def __init__(self, spec1: ComplianceSpecification, spec2: ComplianceSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ComplianceEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotComplianceSpecification(ComplianceSpecification):
    def __init__(self, spec: ComplianceSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: ComplianceEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
