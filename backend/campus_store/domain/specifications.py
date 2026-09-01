"""
Campus Store & Cafeteria POS — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for campus_store.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.campus_store.domain.entities import CampusStoreEntity

class CampusStoreSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: CampusStoreEntity) -> bool:
        pass

    def and_spec(self, other: "CampusStoreSpecification") -> "CampusStoreSpecification":
        return AndCampusStoreSpecification(self, other)

    def or_spec(self, other: "CampusStoreSpecification") -> "CampusStoreSpecification":
        return OrCampusStoreSpecification(self, other)

    def not_spec(self) -> "CampusStoreSpecification":
        return NotCampusStoreSpecification(self)

class ActiveCampusStoreSpecification(CampusStoreSpecification):
    def is_satisfied_by(self, candidate: CampusStoreEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingCampusStoreSpecification(CampusStoreSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: CampusStoreEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndCampusStoreSpecification(CampusStoreSpecification):
    def __init__(self, spec1: CampusStoreSpecification, spec2: CampusStoreSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: CampusStoreEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrCampusStoreSpecification(CampusStoreSpecification):
    def __init__(self, spec1: CampusStoreSpecification, spec2: CampusStoreSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: CampusStoreEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotCampusStoreSpecification(CampusStoreSpecification):
    def __init__(self, spec: CampusStoreSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: CampusStoreEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
