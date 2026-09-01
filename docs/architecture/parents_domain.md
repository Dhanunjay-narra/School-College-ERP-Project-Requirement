# Parent & Guardian Management Domain Architecture

## 1. Domain Overview
The `parents` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `ParentsEntity`
- **Domain Events**: `ParentsCreatedEvent`, `ParentsUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateParentsCommand`
- `UpdateParentsCommand`
- `DeleteParentsCommand`
- `GetParentsByIdQuery`
- `ListParentssQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
