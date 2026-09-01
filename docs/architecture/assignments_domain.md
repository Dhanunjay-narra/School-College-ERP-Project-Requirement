# LMS & Assignments Domain Architecture

## 1. Domain Overview
The `assignments` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `AssignmentsEntity`
- **Domain Events**: `AssignmentsCreatedEvent`, `AssignmentsUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateAssignmentsCommand`
- `UpdateAssignmentsCommand`
- `DeleteAssignmentsCommand`
- `GetAssignmentsByIdQuery`
- `ListAssignmentssQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
