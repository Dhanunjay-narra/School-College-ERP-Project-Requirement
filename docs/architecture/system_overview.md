# Enterprise School & College ERP — System Architecture Manual

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
