# Immutable Audit Logging Domain Architecture

## 1. Domain Overview
The `audit` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `AuditEntity`
- **Domain Events**: `AuditCreatedEvent`, `AuditUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateAuditCommand`
- `UpdateAuditCommand`
- `DeleteAuditCommand`
- `GetAuditByIdQuery`
- `ListAuditsQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
