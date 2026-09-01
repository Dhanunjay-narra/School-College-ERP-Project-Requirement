"""
Applicant Tracking System — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for recruitment.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.recruitment.domain.entities import RecruitmentEntity

class RecruitmentSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: RecruitmentEntity) -> bool:
        pass

    def and_spec(self, other: "RecruitmentSpecification") -> "RecruitmentSpecification":
        return AndRecruitmentSpecification(self, other)

    def or_spec(self, other: "RecruitmentSpecification") -> "RecruitmentSpecification":
        return OrRecruitmentSpecification(self, other)

    def not_spec(self) -> "RecruitmentSpecification":
        return NotRecruitmentSpecification(self)

class ActiveRecruitmentSpecification(RecruitmentSpecification):
    def is_satisfied_by(self, candidate: RecruitmentEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingRecruitmentSpecification(RecruitmentSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: RecruitmentEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndRecruitmentSpecification(RecruitmentSpecification):
    def __init__(self, spec1: RecruitmentSpecification, spec2: RecruitmentSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: RecruitmentEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrRecruitmentSpecification(RecruitmentSpecification):
    def __init__(self, spec1: RecruitmentSpecification, spec2: RecruitmentSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: RecruitmentEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotRecruitmentSpecification(RecruitmentSpecification):
    def __init__(self, spec: RecruitmentSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: RecruitmentEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
