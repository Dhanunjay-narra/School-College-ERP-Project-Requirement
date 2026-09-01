-- Faculty & Workload Management Production Seed Data
INSERT INTO erp_faculty_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('FACU-001', 'default_institution', 'FACU-STD-01', 'Primary Active Faculty & Workload Management Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('FACU-002', 'default_institution', 'FACU-STD-02', 'Secondary Verified Faculty & Workload Management Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('FACU-003', 'default_institution', 'FACU-STD-03', 'Historical Archived Faculty & Workload Management Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
