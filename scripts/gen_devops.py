from writer_util import write_f

def generate_devops_and_docs():
    print("[DEVOPS & DOCS] Generating Infrastructure, CI/CD, and Documentation...")

    # Dockerfile Backend
    write_f("infrastructure/docker/Dockerfile", '''FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ backend/
COPY database/ database/

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
''')

    # Dockerfile Frontend
    write_f("infrastructure/docker/Dockerfile.frontend", '''FROM node:20-alpine AS build

WORKDIR /app
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm install

COPY frontend/ .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY infrastructure/docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
''')

    # docker-compose.yml
    write_f("docker-compose.yml", '''version: '3.8'

services:
  postgres:
    image: postgres:16-alpine
    container_name: erp-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgrespassword
      POSTGRES_DB: school_college_erp
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    container_name: erp-redis
    restart: unless-stopped
    ports:
      - "6379:6379"

  backend:
    build:
      context: .
      dockerfile: infrastructure/docker/Dockerfile
    container_name: erp-backend
    restart: unless-stopped
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql+asyncpg://postgres:postgrespassword@postgres:5432/school_college_erp
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=enterprise-production-super-secret-key-2026
    depends_on:
      - postgres
      - redis

  frontend:
    build:
      context: .
      dockerfile: infrastructure/docker/Dockerfile.frontend
    container_name: erp-frontend
    restart: unless-stopped
    ports:
      - "3000:80"
    depends_on:
      - backend

volumes:
  postgres_data:
''')

    # Kubernetes Manifests
    write_f("infrastructure/kubernetes/backend-deployment.yaml", '''apiVersion: apps/v1
kind: Deployment
metadata:
  name: erp-backend
  labels:
    app: erp-backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: erp-backend
  template:
    metadata:
      labels:
        app: erp-backend
    spec:
      containers:
      - name: erp-backend
        image: erp/backend:1.0.0
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: erp-secrets
              key: database-url
        resources:
          limits:
            cpu: "1000m"
            memory: "1024Mi"
          requests:
            cpu: "250m"
            memory: "256Mi"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 15
          periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: erp-backend-service
spec:
  selector:
    app: erp-backend
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
''')

    # CI/CD GitHub Actions Workflow
    write_f(".github/workflows/ci-cd.yml", '''name: Enterprise ERP CI/CD Pipeline

on:
  push:
    branches: [ main, develop, 'feat/**' ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Test Suite
        run: |
          pytest tests/ --cov=backend

  build-frontend:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Node.js 20
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Build Frontend Application
        run: |
          cd frontend
          npm install
          npm run build
''')

    # Makefile
    write_f("Makefile", '''.PHONY: help install test run-backend run-frontend docker-up docker-down

help:
	@echo "Enterprise School & College ERP - Developer Commands"
	@echo "  make install       Install python and node dependencies"
	@echo "  make test          Run pytest suite"
	@echo "  make run-backend   Start FastAPI server"
	@echo "  make run-frontend  Start Vite development server"
	@echo "  make docker-up     Start complete docker-compose stack"

install:
	pip install -r requirements.txt
	cd frontend && npm install

test:
	pytest tests/ -v

run-backend:
	uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

run-frontend:
	cd frontend && npm run dev

docker-up:
	docker-compose up -d --build

docker-down:
	docker-compose down
''')

    # README.md
    write_f("README.md", '''# Enterprise Unified School & College ERP Platform

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
''')

    print("[DEVOPS & DOCS] Complete infrastructure and documentation generated.")

if __name__ == '__main__':
    generate_devops_and_docs()
