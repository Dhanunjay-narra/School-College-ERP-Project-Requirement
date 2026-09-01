# Enterprise ERP — REST API Playbook & Reference Manual

## 1. Authentication Endpoints
- `POST /api/v1/auth/login`: Authenticate with email/password and obtain JWT bearer tokens.
- `POST /api/v1/auth/register`: Create a new user account.
- `GET /api/v1/auth/me`: Retrieve current authenticated user profile.
- `GET /api/v1/auth/users`: List users within tenant boundary.

## 2. Organization & Campus Endpoints
- `GET /api/v1/organization/institution`: Retrieve institution metadata.
- `GET /api/v1/organization/campuses`: List campuses and geographic branches.
- `GET /api/v1/organization/departments`: List academic and administrative departments.
- `GET /api/v1/organization/rooms`: List lecture halls, classrooms, and labs.

## 3. Academics & Timetable Endpoints
- `GET /api/v1/academics/courses`: List semester courses and faculty assignments.
- `GET /api/v1/academics/timetable`: Get conflict-free timetable slots.

## 4. Student Lifecycle Endpoints
- `GET /api/v1/students/`: List enrolled students with roll numbers and CGPA.
- `GET /api/v1/students/{student_id}`: Retrieve detailed student academic profile.

## 5. Fees & Invoicing Endpoints
- `GET /api/v1/fees/invoices`: List student fee invoices, balances, and payment statuses.
- `GET /api/v1/payments/transactions`: View payment gateway transaction audit logs.

## 6. General Ledger Endpoints
- `GET /api/v1/finance/summary`: Executive YTD revenue, expense, and surplus totals.
- `GET /api/v1/finance/chart-of-accounts`: Standard chart of accounts with balances.

## 7. Operations & Platform Endpoints
- `GET /api/v1/hr/employees`: Employee directory and leave balances.
- `GET /api/v1/library/books`: ISBN catalog and book availability.
- `GET /api/v1/transport/routes`: Bus routes, stops, and live GPS coordinates.
- `GET /api/v1/hostels/rooms`: Hostel blocks and bed occupancy.
- `GET /api/v1/ai/insights`: Predictive machine learning intelligence feed.
- `GET /api/v1/compliance/audit-logs`: Immutable system audit trail.
