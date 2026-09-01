"""
Universal Multi-Channel Notifications — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for communication.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.communication.domain.entities import CommunicationEntity

class CommunicationSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: CommunicationEntity) -> bool:
        pass

    def and_spec(self, other: "CommunicationSpecification") -> "CommunicationSpecification":
        return AndCommunicationSpecification(self, other)

    def or_spec(self, other: "CommunicationSpecification") -> "CommunicationSpecification":
        return OrCommunicationSpecification(self, other)

    def not_spec(self) -> "CommunicationSpecification":
        return NotCommunicationSpecification(self)

class ActiveCommunicationSpecification(CommunicationSpecification):
    def is_satisfied_by(self, candidate: CommunicationEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingCommunicationSpecification(CommunicationSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: CommunicationEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndCommunicationSpecification(CommunicationSpecification):
    def __init__(self, spec1: CommunicationSpecification, spec2: CommunicationSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: CommunicationEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrCommunicationSpecification(CommunicationSpecification):
    def __init__(self, spec1: CommunicationSpecification, spec2: CommunicationSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: CommunicationEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotCommunicationSpecification(CommunicationSpecification):
    def __init__(self, spec: CommunicationSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: CommunicationEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
