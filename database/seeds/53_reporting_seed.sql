-- Universal Enterprise Reporting Production Seed Data
INSERT INTO erp_reporting_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('REPO-001', 'default_institution', 'REPO-STD-01', 'Primary Active Universal Enterprise Reporting Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('REPO-002', 'default_institution', 'REPO-STD-02', 'Secondary Verified Universal Enterprise Reporting Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('REPO-003', 'default_institution', 'REPO-STD-03', 'Historical Archived Universal Enterprise Reporting Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
