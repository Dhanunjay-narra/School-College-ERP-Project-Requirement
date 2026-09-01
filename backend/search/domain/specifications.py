"""
Centralized Faceted Search — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for search.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.search.domain.entities import SearchEntity

class SearchSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: SearchEntity) -> bool:
        pass

    def and_spec(self, other: "SearchSpecification") -> "SearchSpecification":
        return AndSearchSpecification(self, other)

    def or_spec(self, other: "SearchSpecification") -> "SearchSpecification":
        return OrSearchSpecification(self, other)

    def not_spec(self) -> "SearchSpecification":
        return NotSearchSpecification(self)

class ActiveSearchSpecification(SearchSpecification):
    def is_satisfied_by(self, candidate: SearchEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingSearchSpecification(SearchSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: SearchEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndSearchSpecification(SearchSpecification):
    def __init__(self, spec1: SearchSpecification, spec2: SearchSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: SearchEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrSearchSpecification(SearchSpecification):
    def __init__(self, spec1: SearchSpecification, spec2: SearchSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: SearchEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotSearchSpecification(SearchSpecification):
    def __init__(self, spec: SearchSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: SearchEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
