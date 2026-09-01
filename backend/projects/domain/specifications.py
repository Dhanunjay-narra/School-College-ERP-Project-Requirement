"""
Campus Infrastructure Projects — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for projects.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.projects.domain.entities import ProjectsEntity

class ProjectsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: ProjectsEntity) -> bool:
        pass

    def and_spec(self, other: "ProjectsSpecification") -> "ProjectsSpecification":
        return AndProjectsSpecification(self, other)

    def or_spec(self, other: "ProjectsSpecification") -> "ProjectsSpecification":
        return OrProjectsSpecification(self, other)

    def not_spec(self) -> "ProjectsSpecification":
        return NotProjectsSpecification(self)

class ActiveProjectsSpecification(ProjectsSpecification):
    def is_satisfied_by(self, candidate: ProjectsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingProjectsSpecification(ProjectsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: ProjectsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndProjectsSpecification(ProjectsSpecification):
    def __init__(self, spec1: ProjectsSpecification, spec2: ProjectsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ProjectsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrProjectsSpecification(ProjectsSpecification):
    def __init__(self, spec1: ProjectsSpecification, spec2: ProjectsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: ProjectsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotProjectsSpecification(ProjectsSpecification):
    def __init__(self, spec: ProjectsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: ProjectsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
