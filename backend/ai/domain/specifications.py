"""
AI/ML Predictive Intelligence — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for ai.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.ai.domain.entities import AiEntity

class AiSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: AiEntity) -> bool:
        pass

    def and_spec(self, other: "AiSpecification") -> "AiSpecification":
        return AndAiSpecification(self, other)

    def or_spec(self, other: "AiSpecification") -> "AiSpecification":
        return OrAiSpecification(self, other)

    def not_spec(self) -> "AiSpecification":
        return NotAiSpecification(self)

class ActiveAiSpecification(AiSpecification):
    def is_satisfied_by(self, candidate: AiEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingAiSpecification(AiSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: AiEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndAiSpecification(AiSpecification):
    def __init__(self, spec1: AiSpecification, spec2: AiSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AiEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrAiSpecification(AiSpecification):
    def __init__(self, spec1: AiSpecification, spec2: AiSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AiEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotAiSpecification(AiSpecification):
    def __init__(self, spec: AiSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: AiEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
