"""
Admissions CRM & Merit Engine — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for admissions.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.admissions.domain.entities import AdmissionsEntity

class AdmissionsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: AdmissionsEntity) -> bool:
        pass

    def and_spec(self, other: "AdmissionsSpecification") -> "AdmissionsSpecification":
        return AndAdmissionsSpecification(self, other)

    def or_spec(self, other: "AdmissionsSpecification") -> "AdmissionsSpecification":
        return OrAdmissionsSpecification(self, other)

    def not_spec(self) -> "AdmissionsSpecification":
        return NotAdmissionsSpecification(self)

class ActiveAdmissionsSpecification(AdmissionsSpecification):
    def is_satisfied_by(self, candidate: AdmissionsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingAdmissionsSpecification(AdmissionsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: AdmissionsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndAdmissionsSpecification(AdmissionsSpecification):
    def __init__(self, spec1: AdmissionsSpecification, spec2: AdmissionsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AdmissionsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrAdmissionsSpecification(AdmissionsSpecification):
    def __init__(self, spec1: AdmissionsSpecification, spec2: AdmissionsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AdmissionsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotAdmissionsSpecification(AdmissionsSpecification):
    def __init__(self, spec: AdmissionsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: AdmissionsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
