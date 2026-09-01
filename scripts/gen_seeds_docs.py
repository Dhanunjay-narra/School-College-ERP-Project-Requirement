from writer_util import write_f

def generate_seeds_and_docs():
    print("[SEEDS & DOCS] Generating extensive SQL seed files and technical manuals...")

    # 1. Academic Structure & Departments Seed
    write_f("database/seeds/01_academic_structure.sql", """-- Academic Structure, Campuses, and Departments Seed Data
INSERT INTO erp_organization_institutions (id, tenant_id, name, code, institution_type, accreditation, affiliation, currency, timezone, contact_email, contact_phone, address)
VALUES ('default_institution', 'default_institution', 'Apex Institute of Technology & Management', 'AITM', 'UNIVERSITY', 'NAAC A++ Grade, NBA Accredited, ISO 9001:2015', 'Apex Technical University', 'INR', 'Asia/Kolkata', 'contact@erp.edu', '+91-11-23456789', 'Institutional Area, Knowledge Park, Tech City')
ON CONFLICT (code) DO NOTHING;

INSERT INTO erp_organization_campuses (id, institution_id, name, code, city, state, is_main_campus)
VALUES 
('CAMPUS-01', 'default_institution', 'Main Academic Campus', 'MAIN', 'Tech City', 'Telangana', TRUE),
('CAMPUS-02', 'default_institution', 'North Research & Innovation Hub', 'NORTH', 'Innovation Corridor', 'Telangana', FALSE),
('CAMPUS-03', 'default_institution', 'South Medical & Life Sciences Campus', 'SOUTH', 'Health Valley', 'Telangana', FALSE)
ON CONFLICT (id) DO NOTHING;
""")

    # 2. Comprehensive Courses Seed
    write_f("database/seeds/02_courses_curriculum.sql", """-- Courses and Curriculum Seed Data
INSERT INTO erp_academics_courses (id, tenant_id, code, title, credits, department_id, semester) VALUES
('CRS-101', 'default_institution', 'CS101', 'Introduction to Computing & Problem Solving', 4, 'CS-DEP', 1),
('CRS-102', 'default_institution', 'CS102', 'Data Structures & Algorithmic Analysis', 4, 'CS-DEP', 2),
('CRS-103', 'default_institution', 'CS103', 'Digital Logic & Computer Organization', 3, 'CS-DEP', 2),
('CRS-201', 'default_institution', 'CS201', 'Object Oriented Software Design', 4, 'CS-DEP', 3),
('CRS-202', 'default_institution', 'CS202', 'Operating Systems & System Programming', 4, 'CS-DEP', 3),
('CRS-203', 'default_institution', 'CS203', 'Discrete Mathematical Structures', 3, 'CS-DEP', 3),
('CRS-401', 'default_institution', 'CS401', 'Distributed Systems & Cloud Computing', 4, 'CS-DEP', 4),
('CRS-402', 'default_institution', 'CS402', 'Artificial Intelligence & Neural Networks', 4, 'CS-DEP', 4),
('CRS-403', 'default_institution', 'CS403', 'Database Engineering & Big Data Systems', 3, 'CS-DEP', 4),
('CRS-404', 'default_institution', 'CS404', 'Enterprise Software Architecture', 3, 'CS-DEP', 4),
('CRS-501', 'default_institution', 'CS501', 'Compiler Design & Language Processors', 4, 'CS-DEP', 5),
('CRS-502', 'default_institution', 'CS502', 'Computer Networks & Security Protocols', 4, 'CS-DEP', 5),
('CRS-503', 'default_institution', 'CS503', 'Cryptographic Engineering & Cyber Defense', 3, 'CS-DEP', 5),
('CRS-601', 'default_institution', 'CS601', 'Machine Learning & Deep Learning Architectures', 4, 'CS-DEP', 6),
('CRS-602', 'default_institution', 'CS602', 'Cloud Native DevOps & Microservices', 3, 'CS-DEP', 6),
('CRS-603', 'default_institution', 'CS603', 'Full Stack Web Engineering', 3, 'CS-DEP', 6),
('CRS-701', 'default_institution', 'CS701', 'Quantum Computing Fundamentals', 3, 'CS-DEP', 7),
('CRS-702', 'default_institution', 'CS702', 'Autonomous Robotics & Computer Vision', 4, 'CS-DEP', 7),
('CRS-801', 'default_institution', 'CS801', 'Capstone Project & Industry Internship', 12, 'CS-DEP', 8);
""")

    # 3. Technical Manuals
    write_f("docs/architecture/system_overview.md", """# Enterprise School & College ERP — System Architecture Manual

## 1. Executive Summary
This document defines the comprehensive architecture of the Enterprise School & College ERP platform, designed to support modern K-12 schools, higher education institutions, autonomous polytechnics, and large multi-campus universities.

## 2. Architectural Paradigm: Modular Monolith (DDD)
The system adopts a modular monolith architecture with strict Domain-Driven Design (DDD) bounded contexts. Each domain subsystem is isolated with clear presentation, application, domain, and infrastructure layers:

```
module/
├── domain/
│   ├── entities/       # Pure aggregate roots and entities
│   ├── value_objects/  # Immutable domain primitives
│   ├── events/         # Domain events emitted on state mutation
│   └── repositories/   # Abstract repository contracts
├── application/
│   ├── commands/       # CQRS mutation commands
│   ├── queries/        # CQRS query models
│   ├── services/       # Domain orchestrators
│   └── handlers/       # Async event & command handlers
├── infrastructure/
│   ├── persistence/    # SQLAlchemy ORM and schema mappings
│   ├── repositories/   # Concrete database data access objects
│   └── integrations/   # External message brokers, caches & adapters
└── presentation/
    ├── api/            # Versioned FastAPI REST endpoints
    ├── schemas/        # Pydantic input/output schemas
    └── serializers/    # PDF, CSV, XML, JSON-LD export routines
```

## 3. High Availability & Disaster Recovery
- **Database**: PostgreSQL with Primary-Replica streaming replication, connection pooling (PgBouncer), and automated Point-in-Time Recovery (PITR).
- **Caching**: Redis cluster for distributed session tokens, role permissions, timetable matrices, and real-time counter rate limits.
- **Event Bus**: Pluggable event bus supporting In-Memory, Redis Pub/Sub, RabbitMQ, and Apache Kafka.
""")

    write_f("docs/security/threat_model_and_hardening.md", """# Enterprise Security Architecture & Threat Model

## 1. Identity & Authentication Architecture
- **Password Storage**: PBKDF2-HMAC-SHA256 with 100,000 rounds and per-user cryptographic salt (Argon2 / BCrypt supported).
- **Token Security**: Cryptographically signed JWT tokens with standard expiration (60-minute access token, 7-day refresh token).
- **MFA / 2FA**: RFC 6238 Time-based One-Time Password (TOTP) algorithm supported across all privileged administrator personas.
- **Account Protection**: Progressive lockout mechanism with maximum 5 failed attempts triggering a 15-minute temporary lockout.

## 2. Multi-Tenant Partitioning & Data Isolation
All database queries enforce strict tenant boundary filtering (`tenant_id`). Cross-tenant leakage is prevented via:
1. Application middleware injection of validated tenant contexts from JWT claims.
2. Repository-level mandatory tenant query constraints.
3. Database level row-level security (RLS) policies in PostgreSQL.
""")

    print("[SEEDS & DOCS] Seeds and architecture documentation generated.")

if __name__ == '__main__':
    generate_seeds_and_docs()
