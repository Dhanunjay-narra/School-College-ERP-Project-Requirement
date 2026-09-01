"""
Library & RFID Circulation — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for library.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.library.domain.entities import LibraryEntity

class LibrarySpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: LibraryEntity) -> bool:
        pass

    def and_spec(self, other: "LibrarySpecification") -> "LibrarySpecification":
        return AndLibrarySpecification(self, other)

    def or_spec(self, other: "LibrarySpecification") -> "LibrarySpecification":
        return OrLibrarySpecification(self, other)

    def not_spec(self) -> "LibrarySpecification":
        return NotLibrarySpecification(self)

class ActiveLibrarySpecification(LibrarySpecification):
    def is_satisfied_by(self, candidate: LibraryEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingLibrarySpecification(LibrarySpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: LibraryEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndLibrarySpecification(LibrarySpecification):
    def __init__(self, spec1: LibrarySpecification, spec2: LibrarySpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: LibraryEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrLibrarySpecification(LibrarySpecification):
    def __init__(self, spec1: LibrarySpecification, spec2: LibrarySpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: LibraryEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotLibrarySpecification(LibrarySpecification):
    def __init__(self, spec: LibrarySpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: LibraryEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
