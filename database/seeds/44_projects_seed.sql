-- Campus Infrastructure Projects Production Seed Data
INSERT INTO erp_projects_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PROJ-001', 'default_institution', 'PROJ-STD-01', 'Primary Active Campus Infrastructure Projects Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PROJ-002', 'default_institution', 'PROJ-STD-02', 'Secondary Verified Campus Infrastructure Projects Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PROJ-003', 'default_institution', 'PROJ-STD-03', 'Historical Archived Campus Infrastructure Projects Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
