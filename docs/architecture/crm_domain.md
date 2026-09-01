# Institutional CRM & Admissions Leads Domain Architecture

## 1. Domain Overview
The `crm` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `CrmEntity`
- **Domain Events**: `CrmCreatedEvent`, `CrmUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateCrmCommand`
- `UpdateCrmCommand`
- `DeleteCrmCommand`
- `GetCrmByIdQuery`
- `ListCrmsQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
