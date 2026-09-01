-- Identity & Access Management Production Seed Data
INSERT INTO erp_identity_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('IDEN-001', 'default_institution', 'IDEN-STD-01', 'Primary Active Identity & Access Management Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('IDEN-002', 'default_institution', 'IDEN-STD-02', 'Secondary Verified Identity & Access Management Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('IDEN-003', 'default_institution', 'IDEN-STD-03', 'Historical Archived Identity & Access Management Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
