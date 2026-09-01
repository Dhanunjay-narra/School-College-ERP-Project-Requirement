from writer_util import write_f

MODULES = [
    ("identity", "Identity & Access Management"),
    ("organization", "Organization & Multi-Campus"),
    ("students", "Student Information & Lifecycle"),
    ("parents", "Parent & Guardian Management"),
    ("admissions", "Admissions CRM & Merit Engine"),
    ("academics", "Academic Structure & Timetable"),
    ("faculty", "Faculty & Workload Management"),
    ("attendance", "Smart Attendance Engine"),
    ("examinations", "Examinations & Grading"),
    ("assignments", "LMS & Assignments"),
    ("fees", "Fees & Student Billing"),
    ("payments", "Payment Abstraction Gateway"),
    ("finance", "Finance & General Ledger"),
    ("accounting", "Accounts Payable & Receivable"),
    ("procurement", "Procurement Management"),
    ("vendors", "Vendor Management & Compliance"),
    ("inventory", "Campus Inventory & Stores"),
    ("warehouses", "Multi-Store Warehouse Management"),
    ("assets", "Asset Lifecycle & Depreciation"),
    ("maintenance", "Campus Facility Maintenance"),
    ("transport", "Transportation & GPS Fleet"),
    ("hostels", "Hostel & Housing Management"),
    ("library", "Library & RFID Circulation"),
    ("hr", "Human Resource & Recruitment"),
    ("recruitment", "Applicant Tracking System"),
    ("payroll", "Integrated Payroll Engine"),
    ("crm", "Institutional CRM & Admissions Leads"),
    ("alumni", "Alumni Network & Relations"),
    ("communication", "Universal Multi-Channel Notifications"),
    ("documents", "Document Management & Signatures"),
    ("workflows", "Configurable Workflow Engine"),
    ("projects", "Campus Infrastructure Projects"),
    ("events", "Campus Events & Conferences"),
    ("research", "Research & Innovation Management"),
    ("campus_store", "Campus Store & Cafeteria POS"),
    ("production", "Campus Workshop & Fab Lab"),
    ("compliance", "Accreditation & Regulatory Compliance"),
    ("audit", "Immutable Audit Logging"),
    ("analytics", "BI & Institutional Analytics"),
    ("ai", "AI/ML Predictive Intelligence"),
    ("reporting", "Universal Enterprise Reporting"),
    ("search", "Centralized Faceted Search")
]

def generate_specs_and_infra():
    print("[SPECS & INFRA] Generating Domain Specifications, SQL seeds 13-40, and Terraform/Helm configs...")

    for mod, title in MODULES:
        c_name = mod.replace('_', ' ').title().replace(' ', '')
        base_dir = f"backend/{mod}"

        # 1. Specification Pattern
        write_f(f"{base_dir}/domain/specifications.py", f'''"""
{title} — Domain Specification Pattern Implementations.
Reusable predicates and composite business criteria for {mod}.
"""
from abc import ABC, abstractmethod
from typing import Any
from backend.{mod}.domain.entities import {c_name}Entity

class {c_name}Specification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate: {c_name}Entity) -> bool:
        pass

    def and_spec(self, other: "{c_name}Specification") -> "{c_name}Specification":
        return And{c_name}Specification(self, other)

    def or_spec(self, other: "{c_name}Specification") -> "{c_name}Specification":
        return Or{c_name}Specification(self, other)

    def not_spec(self) -> "{c_name}Specification":
        return Not{c_name}Specification(self)

class Active{c_name}Specification({c_name}Specification):
    def is_satisfied_by(self, candidate: {c_name}Entity) -> bool:
        return candidate.status.upper() == "ACTIVE"

class TenantMatching{c_name}Specification({c_name}Specification):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    def is_satisfied_by(self, candidate: {c_name}Entity) -> bool:
        return candidate.tenant_id == self.tenant_id

class And{c_name}Specification({c_name}Specification):
    def __init__(self, spec1: {c_name}Specification, spec2: {c_name}Specification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: {c_name}Entity) -> bool:
        return self.spec1.is_satisfied_by(candidate) and self.spec2.is_satisfied_by(candidate)

class Or{c_name}Specification({c_name}Specification):
    def __init__(self, spec1: {c_name}Specification, spec2: {c_name}Specification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied_by(self, candidate: {c_name}Entity) -> bool:
        return self.spec1.is_satisfied_by(candidate) or self.spec2.is_satisfied_by(candidate)

class Not{c_name}Specification({c_name}Specification):
    def __init__(self, spec: {c_name}Specification):
        self.spec = spec

    def is_satisfied_by(self, candidate: {c_name}Entity) -> bool:
        return not self.spec.is_satisfied_by(candidate)
''')

    # Seed SQL files for all 40 modules
    for i, (mod, title) in enumerate(MODULES, start=13):
        write_f(f"database/seeds/{i:02d}_{mod}_seed.sql", f"""-- {title} Production Seed Data
INSERT INTO erp_{mod}_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('{mod.upper()[:4]}-001', 'default_institution', '{mod.upper()[:4]}-STD-01', 'Primary Active {title} Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('{mod.upper()[:4]}-002', 'default_institution', '{mod.upper()[:4]}-STD-02', 'Secondary Verified {title} Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('{mod.upper()[:4]}-003', 'default_institution', '{mod.upper()[:4]}-STD-03', 'Historical Archived {title} Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
""")

    # Terraform AWS Production Infrastructure
    write_f("infrastructure/terraform/main.tf", """terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC & Networking
resource "aws_vpc" "erp_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  tags = {
    Name        = "school-college-erp-vpc"
    Environment = var.environment
  }
}

resource "aws_subnet" "public_a" {
  vpc_id            = aws_vpc.erp_vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "${var.aws_region}a"
}

resource "aws_subnet" "public_b" {
  vpc_id            = aws_vpc.erp_vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "${var.aws_region}b"
}

# RDS PostgreSQL Multi-AZ
resource "aws_db_instance" "erp_postgres" {
  identifier        = "erp-postgresql-prod"
  engine            = "postgres"
  engine_version    = "16.2"
  instance_class    = "db.r6g.xlarge"
  allocated_storage = 100
  storage_type      = "gp3"
  multi_az          = true
  username          = "erpadmin"
  password          = var.db_password
  skip_final_snapshot = true
}

# ElastiCache Redis Cluster
resource "aws_elasticache_cluster" "erp_redis" {
  cluster_id           = "erp-redis-cluster"
  engine               = "redis"
  node_type            = "cache.r6g.large"
  num_cache_nodes      = 2
  parameter_group_name = "default.redis7"
  port                 = 6379
}

# S3 Document Vault
resource "aws_s3_bucket" "erp_documents" {
  bucket = "enterprise-erp-document-vault-prod"
}
""")

    write_f("infrastructure/terraform/variables.tf", """variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "environment" {
  type    = string
  default = "production"
}

variable "db_password" {
  type      = string
  sensitive = true
  default   = "SuperSecurePostgresDBPassword2026!"
}
""")

    # Helm Chart for Kubernetes
    write_f("infrastructure/helm/Chart.yaml", """apiVersion: v2
name: school-college-erp
description: Helm Chart for Enterprise Unified School & College ERP Platform
type: application
version: 1.0.0
appVersion: "1.0.0"
""")

    write_f("infrastructure/helm/values.yaml", """replicaCount: 3

image:
  repository: erp/backend
  pullPolicy: IfNotPresent
  tag: "1.0.0"

service:
  type: ClusterIP
  port: 8000

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: erp.institution.edu
      paths:
        - path: /
          pathType: ImplementationSpecific

resources:
  limits:
    cpu: 1000m
    memory: 1024Mi
  requests:
    cpu: 250m
    memory: 256Mi

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 75
""")

    print("[SPECS & INFRA] Domain specifications, SQL seeds, and Terraform/Helm configs generated.")

if __name__ == '__main__':
    generate_specs_and_infra()
