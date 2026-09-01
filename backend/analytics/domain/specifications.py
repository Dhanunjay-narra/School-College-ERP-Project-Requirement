"""
BI & Institutional Analytics — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for analytics.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.analytics.domain.entities import AnalyticsEntity

class AnalyticsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: AnalyticsEntity) -> bool:
        pass

    def and_spec(self, other: "AnalyticsSpecification") -> "AnalyticsSpecification":
        return AndAnalyticsSpecification(self, other)

    def or_spec(self, other: "AnalyticsSpecification") -> "AnalyticsSpecification":
        return OrAnalyticsSpecification(self, other)

    def not_spec(self) -> "AnalyticsSpecification":
        return NotAnalyticsSpecification(self)

class ActiveAnalyticsSpecification(AnalyticsSpecification):
    def is_satisfied_by(self, candidate: AnalyticsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingAnalyticsSpecification(AnalyticsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: AnalyticsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndAnalyticsSpecification(AnalyticsSpecification):
    def __init__(self, spec1: AnalyticsSpecification, spec2: AnalyticsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AnalyticsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrAnalyticsSpecification(AnalyticsSpecification):
    def __init__(self, spec1: AnalyticsSpecification, spec2: AnalyticsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AnalyticsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotAnalyticsSpecification(AnalyticsSpecification):
    def __init__(self, spec: AnalyticsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: AnalyticsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
