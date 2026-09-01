# Research & Innovation Management Domain Architecture

## 1. Domain Overview
The `research` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `ResearchEntity`
- **Domain Events**: `ResearchCreatedEvent`, `ResearchUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateResearchCommand`
- `UpdateResearchCommand`
- `DeleteResearchCommand`
- `GetResearchByIdQuery`
- `ListResearchsQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
