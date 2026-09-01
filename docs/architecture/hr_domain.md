# Human Resource & Recruitment Domain Architecture

## 1. Domain Overview
The `hr` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `HrEntity`
- **Domain Events**: `HrCreatedEvent`, `HrUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateHrCommand`
- `UpdateHrCommand`
- `DeleteHrCommand`
- `GetHrByIdQuery`
- `ListHrsQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
