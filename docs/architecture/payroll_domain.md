# Integrated Payroll Engine Domain Architecture

## 1. Domain Overview
The `payroll` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `PayrollEntity`
- **Domain Events**: `PayrollCreatedEvent`, `PayrollUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreatePayrollCommand`
- `UpdatePayrollCommand`
- `DeletePayrollCommand`
- `GetPayrollByIdQuery`
- `ListPayrollsQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
