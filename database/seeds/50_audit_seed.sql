-- Immutable Audit Logging Production Seed Data
INSERT INTO erp_audit_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('AUDI-001', 'default_institution', 'AUDI-STD-01', 'Primary Active Immutable Audit Logging Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('AUDI-002', 'default_institution', 'AUDI-STD-02', 'Secondary Verified Immutable Audit Logging Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('AUDI-003', 'default_institution', 'AUDI-STD-03', 'Historical Archived Immutable Audit Logging Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
