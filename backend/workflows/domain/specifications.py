"""
Configurable Workflow Engine — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for workflows.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.workflows.domain.entities import WorkflowsEntity

class WorkflowsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: WorkflowsEntity) -> bool:
        pass

    def and_spec(self, other: "WorkflowsSpecification") -> "WorkflowsSpecification":
        return AndWorkflowsSpecification(self, other)

    def or_spec(self, other: "WorkflowsSpecification") -> "WorkflowsSpecification":
        return OrWorkflowsSpecification(self, other)

    def not_spec(self) -> "WorkflowsSpecification":
        return NotWorkflowsSpecification(self)

class ActiveWorkflowsSpecification(WorkflowsSpecification):
    def is_satisfied_by(self, candidate: WorkflowsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingWorkflowsSpecification(WorkflowsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: WorkflowsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndWorkflowsSpecification(WorkflowsSpecification):
    def __init__(self, spec1: WorkflowsSpecification, spec2: WorkflowsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: WorkflowsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrWorkflowsSpecification(WorkflowsSpecification):
    def __init__(self, spec1: WorkflowsSpecification, spec2: WorkflowsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: WorkflowsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotWorkflowsSpecification(WorkflowsSpecification):
    def __init__(self, spec: WorkflowsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: WorkflowsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
