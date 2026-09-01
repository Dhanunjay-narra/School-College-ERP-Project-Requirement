"""
Universal Enterprise Reporting — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for reporting.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.reporting.domain.entities import ReportingEntity

class ReportingSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: ReportingEntity) -> bool:
        pass

    def and_spec(self, other: "ReportingSpecification") -> "ReportingSpecification":
        return AndReportingSpecification(self, other)

    def or_spec(self, other: "ReportingSpecification") -> "ReportingSpecification":
        return OrReportingSpecification(self, other)

    def not_spec(self) -> "ReportingSpecification":
        return NotReportingSpecification(self)

class ActiveReportingSpecification(ReportingSpecification):
    def is_satisfied_by(self, candidate: ReportingEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingReportingSpecification(ReportingSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: ReportingEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndReportingSpecification(ReportingSpecification):
    def __init__(self, spec1: ReportingSpecification, spec2: ReportingSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ReportingEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrReportingSpecification(ReportingSpecification):
    def __init__(self, spec1: ReportingSpecification, spec2: ReportingSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ReportingEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotReportingSpecification(ReportingSpecification):
    def __init__(self, spec: ReportingSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: ReportingEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
