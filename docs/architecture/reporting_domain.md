# Universal Enterprise Reporting Domain Architecture

## 1. Domain Overview
The `reporting` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `ReportingEntity`
- **Domain Events**: `ReportingCreatedEvent`, `ReportingUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateReportingCommand`
- `UpdateReportingCommand`
- `DeleteReportingCommand`
- `GetReportingByIdQuery`
- `ListReportingsQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
