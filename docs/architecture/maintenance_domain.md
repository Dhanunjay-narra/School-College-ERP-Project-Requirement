# Campus Facility Maintenance Domain Architecture

## 1. Domain Overview
The `maintenance` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `MaintenanceEntity`
- **Domain Events**: `MaintenanceCreatedEvent`, `MaintenanceUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateMaintenanceCommand`
- `UpdateMaintenanceCommand`
- `DeleteMaintenanceCommand`
- `GetMaintenanceByIdQuery`
- `ListMaintenancesQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
