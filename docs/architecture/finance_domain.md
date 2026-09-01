# Finance & General Ledger Domain Architecture

## 1. Domain Overview
The `finance` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `FinanceEntity`
- **Domain Events**: `FinanceCreatedEvent`, `FinanceUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateFinanceCommand`
- `UpdateFinanceCommand`
- `DeleteFinanceCommand`
- `GetFinanceByIdQuery`
- `ListFinancesQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
