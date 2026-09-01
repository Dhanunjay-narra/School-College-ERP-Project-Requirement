-- Human Resource & Recruitment Production Seed Data
INSERT INTO erp_hr_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('HR-001', 'default_institution', 'HR-STD-01', 'Primary Active Human Resource & Recruitment Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('HR-002', 'default_institution', 'HR-STD-02', 'Secondary Verified Human Resource & Recruitment Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('HR-003', 'default_institution', 'HR-STD-03', 'Historical Archived Human Resource & Recruitment Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
