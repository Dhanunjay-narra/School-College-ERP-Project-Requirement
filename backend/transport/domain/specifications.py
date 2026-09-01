"""
Transportation & GPS Fleet — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for transport.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.transport.domain.entities import TransportEntity

class TransportSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: TransportEntity) -> bool:
        pass

    def and_spec(self, other: "TransportSpecification") -> "TransportSpecification":
        return AndTransportSpecification(self, other)

    def or_spec(self, other: "TransportSpecification") -> "TransportSpecification":
        return OrTransportSpecification(self, other)

    def not_spec(self) -> "TransportSpecification":
        return NotTransportSpecification(self)

class ActiveTransportSpecification(TransportSpecification):
    def is_satisfied_by(self, candidate: TransportEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingTransportSpecification(TransportSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: TransportEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndTransportSpecification(TransportSpecification):
    def __init__(self, spec1: TransportSpecification, spec2: TransportSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: TransportEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrTransportSpecification(TransportSpecification):
    def __init__(self, spec1: TransportSpecification, spec2: TransportSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: TransportEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotTransportSpecification(TransportSpecification):
    def __init__(self, spec: TransportSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: TransportEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
