# Library & RFID Circulation Domain Architecture

## 1. Domain Overview
The `library` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `LibraryEntity`
- **Domain Events**: `LibraryCreatedEvent`, `LibraryUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateLibraryCommand`
- `UpdateLibraryCommand`
- `DeleteLibraryCommand`
- `GetLibraryByIdQuery`
- `ListLibrarysQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
