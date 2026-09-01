terraform {
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
