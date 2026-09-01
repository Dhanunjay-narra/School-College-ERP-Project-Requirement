"""
Campus Events & Conferences — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for events.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.events.domain.entities import EventsEntity

class EventsSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: EventsEntity) -> bool:
        pass

    def and_spec(self, other: "EventsSpecification") -> "EventsSpecification":
        return AndEventsSpecification(self, other)

    def or_spec(self, other: "EventsSpecification") -> "EventsSpecification":
        return OrEventsSpecification(self, other)

    def not_spec(self) -> "EventsSpecification":
        return NotEventsSpecification(self)

class ActiveEventsSpecification(EventsSpecification):
    def is_satisfied_by(self, candidate: EventsEntity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatchingEventsSpecification(EventsSpecification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: EventsEntity) -> bool:
        return candidate.tenant_id == self.tenant_id

class AndEventsSpecification(EventsSpecification):
    def __init__(self, spec1: EventsSpecification, spec2: EventsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: EventsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class OrEventsSpecification(EventsSpecification):
    def __init__(self, spec1: EventsSpecification, spec2: EventsSpecification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: EventsEntity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class NotEventsSpecification(EventsSpecification):
    def __init__(self, spec: EventsSpecification):
        self.spec = spec

    def is_satisfied_by(self, candidate: EventsEntity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
