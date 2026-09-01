# Organization & Multi-Campus Domain Architecture

## 1. Domain Overview
The `organization` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `OrganizationEntity`
- **Domain Events**: `OrganizationCreatedEvent`, `OrganizationUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateOrganizationCommand`
- `UpdateOrganizationCommand`
- `DeleteOrganizationCommand`
- `GetOrganizationByIdQuery`
- `ListOrganizationsQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
