"""
Document Management & Signatures — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for documents.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.documents.domain.entities import DocumentsEntity

class DocumentsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: DocumentsEntity) -> bool:
        pass

    def and_spec(self, other: "DocumentsSpecification") -> "DocumentsSpecification":
        return AndDocumentsSpecification(self, other)

    def or_spec(self, other: "DocumentsSpecification") -> "DocumentsSpecification":
        return OrDocumentsSpecification(self, other)

    def not_spec(self) -> "DocumentsSpecification":
        return NotDocumentsSpecification(self)

class ActiveDocumentsSpecification(DocumentsSpecification):
    def is_satisfied_by(self, candidate: DocumentsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingDocumentsSpecification(DocumentsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: DocumentsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndDocumentsSpecification(DocumentsSpecification):
    def __init__(self, spec1: DocumentsSpecification, spec2: DocumentsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: DocumentsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrDocumentsSpecification(DocumentsSpecification):
    def __init__(self, spec1: DocumentsSpecification, spec2: DocumentsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: DocumentsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotDocumentsSpecification(DocumentsSpecification):
    def __init__(self, spec: DocumentsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: DocumentsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
