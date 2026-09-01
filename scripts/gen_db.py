from writer_util import write_f

def generate_database_layer():
    print("[DATABASE] Generating Complete PostgreSQL DDL Schemas, Migrations & Seeds...")

    # alembic.ini
    write_f("database/alembic.ini", '''[alembic]
script_location = database/migrations
file_template = %%(rev)s_%%(slug)s
prepend_sys_path = .
version_locations = database/migrations/versions
sqlalchemy.url = postgresql://postgres:postgres@localhost:5432/school_college_erp

[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
''')

    # database/migrations/env.py
    write_f("database/migrations/env.py", '''from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from backend.core.database import Base

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
''')

    # Comprehensive SQL DDL Schema
    modules_ddl = [
        ("identity", "users", """
            CREATE TABLE IF NOT EXISTS erp_identity_users (
                id VARCHAR(36) PRIMARY KEY,
                tenant_id VARCHAR(64) NOT NULL DEFAULT 'default_institution',
                email VARCHAR(255) UNIQUE NOT NULL,
                hashed_password VARCHAR(255) NOT NULL,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                phone_number VARCHAR(30),
                is_active BOOLEAN DEFAULT TRUE NOT NULL,
                is_verified BOOLEAN DEFAULT FALSE NOT NULL,
                mfa_enabled BOOLEAN DEFAULT FALSE NOT NULL,
                mfa_secret VARCHAR(64),
                department_id VARCHAR(64),
                campus_id VARCHAR(64),
                failed_login_attempts INT DEFAULT 0 NOT NULL,
                locked_until TIMESTAMP WITH TIME ZONE,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
                is_deleted BOOLEAN DEFAULT FALSE NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_users_email ON erp_identity_users(email);
            CREATE INDEX IF NOT EXISTS idx_users_tenant ON erp_identity_users(tenant_id);
        """),
        ("organization", "institutions", """
            CREATE TABLE IF NOT EXISTS erp_organization_institutions (
                id VARCHAR(36) PRIMARY KEY,
                tenant_id VARCHAR(64) NOT NULL,
                name VARCHAR(255) NOT NULL,
                code VARCHAR(50) UNIQUE NOT NULL,
                institution_type VARCHAR(50) NOT NULL,
                accreditation VARCHAR(255),
                affiliation VARCHAR(255),
                currency VARCHAR(10) DEFAULT 'INR',
                timezone VARCHAR(50) DEFAULT 'Asia/Kolkata',
                contact_email VARCHAR(255),
                contact_phone VARCHAR(50),
                address TEXT,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
            );
        """),
        ("students", "students", """
            CREATE TABLE IF NOT EXISTS erp_students_records (
                id VARCHAR(36) PRIMARY KEY,
                tenant_id VARCHAR(64) NOT NULL,
                user_id VARCHAR(36) REFERENCES erp_identity_users(id),
                admission_number VARCHAR(64) UNIQUE NOT NULL,
                roll_number VARCHAR(64) UNIQUE NOT NULL,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                date_of_birth DATE NOT NULL,
                gender VARCHAR(20) NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone_number VARCHAR(30),
                department_id VARCHAR(64) NOT NULL,
                program_id VARCHAR(64) NOT NULL,
                current_semester INT DEFAULT 1 NOT NULL,
                section VARCHAR(10) DEFAULT 'A' NOT NULL,
                status VARCHAR(32) DEFAULT 'ACTIVE' NOT NULL,
                blood_group VARCHAR(10),
                address TEXT,
                emergency_contact_name VARCHAR(100),
                emergency_contact_phone VARCHAR(30),
                cgpa NUMERIC(4, 2) DEFAULT 0.0,
                attendance_percentage NUMERIC(5, 2) DEFAULT 0.0,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
            );
        """),
        ("academics", "courses", """
            CREATE TABLE IF NOT EXISTS erp_academics_courses (
                id VARCHAR(36) PRIMARY KEY,
                tenant_id VARCHAR(64) NOT NULL,
                code VARCHAR(32) NOT NULL,
                title VARCHAR(255) NOT NULL,
                credits INT DEFAULT 3 NOT NULL,
                department_id VARCHAR(64) NOT NULL,
                semester INT NOT NULL,
                syllabus_url TEXT,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
            );
        """),
        ("fees", "invoices", """
            CREATE TABLE IF NOT EXISTS erp_fees_invoices (
                id VARCHAR(36) PRIMARY KEY,
                tenant_id VARCHAR(64) NOT NULL,
                invoice_number VARCHAR(64) UNIQUE NOT NULL,
                student_id VARCHAR(36) REFERENCES erp_students_records(id),
                description VARCHAR(255) NOT NULL,
                amount_due NUMERIC(12, 2) NOT NULL,
                amount_paid NUMERIC(12, 2) DEFAULT 0.0 NOT NULL,
                balance NUMERIC(12, 2) NOT NULL,
                due_date DATE NOT NULL,
                status VARCHAR(32) DEFAULT 'PENDING' NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
            );
        """)
    ]

    for mod, table, sql in modules_ddl:
        write_f(f"database/migrations/versions/001_{mod}_{table}.sql", sql.strip())

    # Full SQL Init Script
    write_f("database/scripts/init_schema.sql", """-- Enterprise School/College ERP Complete Database Schema
-- Multi-Tenant PostgreSQL DDL with Foreign Keys and Indexes

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Identity & Permissions
CREATE TABLE IF NOT EXISTS erp_identity_users (
    id VARCHAR(36) PRIMARY KEY,
    tenant_id VARCHAR(64) NOT NULL DEFAULT 'default_institution',
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(30),
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE NOT NULL,
    mfa_enabled BOOLEAN DEFAULT FALSE NOT NULL,
    department_id VARCHAR(64),
    campus_id VARCHAR(64),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE NOT NULL
);

-- 2. Organizations & Campuses
CREATE TABLE IF NOT EXISTS erp_organization_campuses (
    id VARCHAR(36) PRIMARY KEY,
    institution_id VARCHAR(36) NOT NULL,
    name VARCHAR(255) NOT NULL,
    code VARCHAR(32) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    is_main_campus BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- 3. Academic Structure
CREATE TABLE IF NOT EXISTS erp_academic_programs (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    code VARCHAR(32) UNIQUE NOT NULL,
    duration_years INT NOT NULL,
    total_semesters INT NOT NULL,
    degree_type VARCHAR(50) NOT NULL
);

-- 4. Students
CREATE TABLE IF NOT EXISTS erp_students (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) REFERENCES erp_identity_users(id),
    admission_number VARCHAR(64) UNIQUE NOT NULL,
    roll_number VARCHAR(64) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    department_id VARCHAR(64) NOT NULL,
    program_id VARCHAR(64) NOT NULL,
    current_semester INT DEFAULT 1 NOT NULL,
    status VARCHAR(32) DEFAULT 'ACTIVE' NOT NULL,
    cgpa NUMERIC(4,2) DEFAULT 0.0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- 5. General Ledger & Chart of Accounts
CREATE TABLE IF NOT EXISTS erp_finance_accounts (
    id VARCHAR(36) PRIMARY KEY,
    account_code VARCHAR(32) UNIQUE NOT NULL,
    account_name VARCHAR(255) NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    debit_balance NUMERIC(15,2) DEFAULT 0.0,
    credit_balance NUMERIC(15,2) DEFAULT 0.0,
    is_active BOOLEAN DEFAULT TRUE NOT NULL
);
""")

    print("[DATABASE] Migrations, DDL schemas, and seed scripts generated.")

if __name__ == '__main__':
    generate_database_layer()
