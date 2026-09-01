# Campus Infrastructure Projects Domain Architecture

## 1. Domain Overview
The `projects` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `ProjectsEntity`
- **Domain Events**: `ProjectsCreatedEvent`, `ProjectsUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateProjectsCommand`
- `UpdateProjectsCommand`
- `DeleteProjectsCommand`
- `GetProjectsByIdQuery`
- `ListProjectssQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
