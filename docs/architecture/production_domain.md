# Campus Workshop & Fab Lab Domain Architecture

## 1. Domain Overview
The `production` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `ProductionEntity`
- **Domain Events**: `ProductionCreatedEvent`, `ProductionUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateProductionCommand`
- `UpdateProductionCommand`
- `DeleteProductionCommand`
- `GetProductionByIdQuery`
- `ListProductionsQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
