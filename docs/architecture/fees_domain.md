# Fees & Student Billing Domain Architecture

## 1. Domain Overview
The `fees` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `FeesEntity`
- **Domain Events**: `FeesCreatedEvent`, `FeesUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateFeesCommand`
- `UpdateFeesCommand`
- `DeleteFeesCommand`
- `GetFeesByIdQuery`
- `ListFeessQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
