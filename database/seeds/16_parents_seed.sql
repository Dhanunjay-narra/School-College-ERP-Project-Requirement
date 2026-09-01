-- Parent & Guardian Management Production Seed Data
INSERT INTO erp_parents_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PARE-001', 'default_institution', 'PARE-STD-01', 'Primary Active Parent & Guardian Management Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PARE-002', 'default_institution', 'PARE-STD-02', 'Secondary Verified Parent & Guardian Management Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PARE-003', 'default_institution', 'PARE-STD-03', 'Historical Archived Parent & Guardian Management Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
