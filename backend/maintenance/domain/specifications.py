"""
Campus Facility Maintenance — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for maintenance.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.maintenance.domain.entities import MaintenanceEntity

class MaintenanceSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: MaintenanceEntity) -> bool:
        pass

    def and_spec(self, other: "MaintenanceSpecification") -> "MaintenanceSpecification":
        return AndMaintenanceSpecification(self, other)

    def or_spec(self, other: "MaintenanceSpecification") -> "MaintenanceSpecification":
        return OrMaintenanceSpecification(self, other)

    def not_spec(self) -> "MaintenanceSpecification":
        return NotMaintenanceSpecification(self)

class ActiveMaintenanceSpecification(MaintenanceSpecification):
    def is_satisfied_by(self, candidate: MaintenanceEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingMaintenanceSpecification(MaintenanceSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: MaintenanceEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndMaintenanceSpecification(MaintenanceSpecification):
    def __init__(self, spec1: MaintenanceSpecification, spec2: MaintenanceSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: MaintenanceEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrMaintenanceSpecification(MaintenanceSpecification):
    def __init__(self, spec1: MaintenanceSpecification, spec2: MaintenanceSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: MaintenanceEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotMaintenanceSpecification(MaintenanceSpecification):
    def __init__(self, spec: MaintenanceSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: MaintenanceEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
