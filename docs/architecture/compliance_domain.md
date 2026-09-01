# Accreditation & Regulatory Compliance Domain Architecture

## 1. Domain Overview
The `compliance` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `ComplianceEntity`
- **Domain Events**: `ComplianceCreatedEvent`, `ComplianceUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateComplianceCommand`
- `UpdateComplianceCommand`
- `DeleteComplianceCommand`
- `GetComplianceByIdQuery`
- `ListCompliancesQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
