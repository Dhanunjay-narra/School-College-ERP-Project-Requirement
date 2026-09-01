# Smart Attendance Engine Domain Architecture

## 1. Domain Overview
The `attendance` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `AttendanceEntity`
- **Domain Events**: `AttendanceCreatedEvent`, `AttendanceUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateAttendanceCommand`
- `UpdateAttendanceCommand`
- `DeleteAttendanceCommand`
- `GetAttendanceByIdQuery`
- `ListAttendancesQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
