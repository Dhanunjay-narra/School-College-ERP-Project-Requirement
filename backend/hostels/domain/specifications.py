"""
Hostel & Housing Management — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for hostels.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.hostels.domain.entities import HostelsEntity

class HostelsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: HostelsEntity) -> bool:
        pass

    def and_spec(self, other: "HostelsSpecification") -> "HostelsSpecification":
        return AndHostelsSpecification(self, other)

    def or_spec(self, other: "HostelsSpecification") -> "HostelsSpecification":
        return OrHostelsSpecification(self, other)

    def not_spec(self) -> "HostelsSpecification":
        return NotHostelsSpecification(self)

class ActiveHostelsSpecification(HostelsSpecification):
    def is_satisfied_by(self, candidate: HostelsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingHostelsSpecification(HostelsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: HostelsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndHostelsSpecification(HostelsSpecification):
    def __init__(self, spec1: HostelsSpecification, spec2: HostelsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: HostelsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrHostelsSpecification(HostelsSpecification):
    def __init__(self, spec1: HostelsSpecification, spec2: HostelsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: HostelsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotHostelsSpecification(HostelsSpecification):
    def __init__(self, spec: HostelsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: HostelsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
