"""
Alumni Network & Relations — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for alumni.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.alumni.domain.entities import AlumniEntity

class AlumniSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: AlumniEntity) -> bool:
        pass

    def and_spec(self, other: "AlumniSpecification") -> "AlumniSpecification":
        return AndAlumniSpecification(self, other)

    def or_spec(self, other: "AlumniSpecification") -> "AlumniSpecification":
        return OrAlumniSpecification(self, other)

    def not_spec(self) -> "AlumniSpecification":
        return NotAlumniSpecification(self)

class ActiveAlumniSpecification(AlumniSpecification):
    def is_satisfied_by(self, candidate: AlumniEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingAlumniSpecification(AlumniSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: AlumniEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndAlumniSpecification(AlumniSpecification):
    def __init__(self, spec1: AlumniSpecification, spec2: AlumniSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AlumniEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrAlumniSpecification(AlumniSpecification):
    def __init__(self, spec1: AlumniSpecification, spec2: AlumniSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: AlumniEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotAlumniSpecification(AlumniSpecification):
    def __init__(self, spec: AlumniSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: AlumniEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
