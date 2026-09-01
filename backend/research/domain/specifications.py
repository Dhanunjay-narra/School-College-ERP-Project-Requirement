"""
Research & Innovation Management — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for research.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.research.domain.entities import ResearchEntity

class ResearchSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: ResearchEntity) -> bool:
        pass

    def and_spec(self, other: "ResearchSpecification") -> "ResearchSpecification":
        return AndResearchSpecification(self, other)

    def or_spec(self, other: "ResearchSpecification") -> "ResearchSpecification":
        return OrResearchSpecification(self, other)

    def not_spec(self) -> "ResearchSpecification":
        return NotResearchSpecification(self)

class ActiveResearchSpecification(ResearchSpecification):
    def is_satisfied_by(self, candidate: ResearchEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingResearchSpecification(ResearchSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: ResearchEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndResearchSpecification(ResearchSpecification):
    def __init__(self, spec1: ResearchSpecification, spec2: ResearchSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ResearchEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrResearchSpecification(ResearchSpecification):
    def __init__(self, spec1: ResearchSpecification, spec2: ResearchSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ResearchEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotResearchSpecification(ResearchSpecification):
    def __init__(self, spec: ResearchSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: ResearchEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
