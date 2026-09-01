-- Accreditation & Regulatory Compliance Production Seed Data
INSERT INTO erp_compliance_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('COMP-001', 'default_institution', 'COMP-STD-01', 'Primary Active Accreditation & Regulatory Compliance Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('COMP-002', 'default_institution', 'COMP-STD-02', 'Secondary Verified Accreditation & Regulatory Compliance Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('COMP-003', 'default_institution', 'COMP-STD-03', 'Historical Archived Accreditation & Regulatory Compliance Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
