# Campus Inventory & Stores Domain Architecture

## 1. Domain Overview
The `inventory` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `InventoryEntity`
- **Domain Events**: `InventoryCreatedEvent`, `InventoryUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateInventoryCommand`
- `UpdateInventoryCommand`
- `DeleteInventoryCommand`
- `GetInventoryByIdQuery`
- `ListInventorysQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
