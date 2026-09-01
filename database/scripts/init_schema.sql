-- Enterprise School/College ERP Complete Database Schema
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
