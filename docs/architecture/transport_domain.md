# Transportation & GPS Fleet Domain Architecture

## 1. Domain Overview
The `transport` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `TransportEntity`
- **Domain Events**: `TransportCreatedEvent`, `TransportUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateTransportCommand`
- `UpdateTransportCommand`
- `DeleteTransportCommand`
- `GetTransportByIdQuery`
- `ListTransportsQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
