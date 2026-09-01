variable "aws_region" {
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
