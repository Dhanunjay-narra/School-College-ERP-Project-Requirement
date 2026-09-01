-- Campus Facility Maintenance Production Seed Data
INSERT INTO erp_maintenance_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('MAIN-001', 'default_institution', 'MAIN-STD-01', 'Primary Active Campus Facility Maintenance Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('MAIN-002', 'default_institution', 'MAIN-STD-02', 'Secondary Verified Campus Facility Maintenance Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('MAIN-003', 'default_institution', 'MAIN-STD-03', 'Historical Archived Campus Facility Maintenance Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
