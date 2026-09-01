# BI & Institutional Analytics Domain Architecture

## 1. Domain Overview
The `analytics` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `AnalyticsEntity`
- **Domain Events**: `AnalyticsCreatedEvent`, `AnalyticsUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateAnalyticsCommand`
- `UpdateAnalyticsCommand`
- `DeleteAnalyticsCommand`
- `GetAnalyticsByIdQuery`
- `ListAnalyticssQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
