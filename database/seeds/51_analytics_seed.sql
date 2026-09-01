-- BI & Institutional Analytics Production Seed Data
INSERT INTO erp_analytics_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ANAL-001', 'default_institution', 'ANAL-STD-01', 'Primary Active BI & Institutional Analytics Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ANAL-002', 'default_institution', 'ANAL-STD-02', 'Secondary Verified BI & Institutional Analytics Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ANAL-003', 'default_institution', 'ANAL-STD-03', 'Historical Archived BI & Institutional Analytics Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
