# Applicant Tracking System Domain Architecture

## 1. Domain Overview
The `recruitment` subsystem provides dedicated business operations, domain entity lifecycles, and event-driven integrations within the Enterprise ERP modular monolith.

## 2. Aggregates & Entities
- **Primary Aggregate**: `RecruitmentEntity`
- **Domain Events**: `RecruitmentCreatedEvent`, `RecruitmentUpdatedEvent`

## 3. CQRS Commands & Queries
- `CreateRecruitmentCommand`
- `UpdateRecruitmentCommand`
- `DeleteRecruitmentCommand`
- `GetRecruitmentByIdQuery`
- `ListRecruitmentsQuery`

## 4. Security & Access Control
All operations are protected via Role-Based Access Control (RBAC) and Tenant-Partitioned Authorization policies.
