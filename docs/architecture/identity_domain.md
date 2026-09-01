# Identity & Access Management Domain Architecture

## 1. Domain Overview
The `identity` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `IdentityEntity`
- **Domain Events**: `IdentityCreatedEvent`, `IdentityUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateIdentityCommand`
- `UpdateIdentityCommand`
- `DeleteIdentityCommand`
- `GetIdentityByIdQuery`
- `ListIdentitysQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
