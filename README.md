# Enterprise Unified School & College ERP Platform

A modern, production-grade, multi-tenant School, College, and University Enterprise Resource Planning (ERP) platform built with a modular monolith Domain-Driven Design (DDD) architecture, FastAPI backend, React + TypeScript + Tailwind CSS frontend, and comprehensive cross-domain workflows.

---

## Architecture Overview

```
                      SCHOOL / COLLEGE ERP
                               │
               ┌───────────────┴───────────────┐
               │          API Gateway          │
               └───────────────┬───────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
   Web Portal             Mobile APIs            Admin Portal
        │                      │                      │
        └──────────────────────┼──────────────────────┘
                               │
                      Application Services
                               │
 ┌───────────┬───────────┬─────┴─────┬───────────┬───────────┐
 │ Student   │ Academic  │  Finance  │    HR     │  Campus   │
 │ Domain    │ Domain    │  Domain   │  Domain   │ Operations│
 └───────────┴───────────┴───────────┴───────────┴───────────┘
                               │
                         Domain Events
                               │
               ┌───────────────┼───────────────┐
               │               │               │
            Database         Cache           Queue
               │                               │
           PostgreSQL                    Event Workers
```

---

## 1-Click Demo Login Credentials

The frontend includes an interactive **1-Click Demo Login Bar** allowing immediate persona switching:

| Role | Demo Email | Persona | Key Capabilities |
| :--- | :--- | :--- | :--- |
| **Super Admin** | `superadmin@erp.edu` | Super Administrator | Multi-tenant setup, global policies, audit logs |
| **Principal** | `principal@erp.edu` | Dr. Rajesh Sharma | Executive KPIs, approvals, department oversight |
| **HOD CS** | `hod.cs@erp.edu` | Prof. Ananya Iyer | Faculty workload, curriculum, approvals |
| **Faculty** | `faculty.smith@erp.edu` | Dr. David Smith | Class timetable, attendance, marks entry, LMS |
| **Student** | `student.aarav@erp.edu` | Aarav Patel | Timetable, grades, fees, attendance, hostel |
| **Parent** | `parent.sharma@erp.edu` | Vikram Sharma | Ward progress, attendance alerts, fee payments |
| **Accountant** | `accountant@erp.edu` | Priya Nair | General Ledger, Invoices, Payment reconciliation |
| **Librarian** | `librarian@erp.edu` | Meenakshi S. | ISBN catalog, RFID circulation, book fines |
| **Hostel Warden**| `warden@erp.edu` | Col. Ramesh Singh | Room & bed allocations, outpasses, mess menu |
| **Transport** | `transport@erp.edu` | Gurpreet Singh | Fleet GPS tracking, bus routes, driver logs |

> **Default Password for All Demo Accounts**: `Password@123`

---

## Installation & Setup

### Prerequisites
- Python 3.12+
- Node.js 20+ & npm
- PostgreSQL 16+ (Optional, in-memory repository fallback included)
- Redis 7+ (Optional, in-memory cache fallback included)

### 1. Backend Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```
API Documentation will be live at: `http://localhost:8000/docs`

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Web Application will be accessible at: `http://localhost:3000`

---

## Build & Docker Deployment

### Docker Compose
```bash
docker-compose up -d --build
```

### Production Build
```bash
cd frontend && npm run build
```

---

## Running Automated Tests

```bash
pytest tests/ -v
```

---

## License & Intellectual Property

PROPRIETARY AND CONFIDENTIAL. All rights reserved.
