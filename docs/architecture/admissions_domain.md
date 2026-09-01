# Admissions CRM & Merit Engine Domain Architecture

## 1. Domain Overview
The `admissions` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `AdmissionsEntity`
- **Domain Events**: `AdmissionsCreatedEvent`, `AdmissionsUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateAdmissionsCommand`
- `UpdateAdmissionsCommand`
- `DeleteAdmissionsCommand`
- `GetAdmissionsByIdQuery`
- `ListAdmissionssQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
