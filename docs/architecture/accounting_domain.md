# Accounts Payable & Receivable Domain Architecture

## 1. Domain Overview
The `accounting` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `AccountingEntity`
- **Domain Events**: `AccountingCreatedEvent`, `AccountingUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateAccountingCommand`
- `UpdateAccountingCommand`
- `DeleteAccountingCommand`
- `GetAccountingByIdQuery`
- `ListAccountingsQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
