-- LMS & Assignments Production Seed Data
INSERT INTO erp_assignments_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ASSI-001', 'default_institution', 'ASSI-STD-01', 'Primary Active LMS & Assignments Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ASSI-002', 'default_institution', 'ASSI-STD-02', 'Secondary Verified LMS & Assignments Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ASSI-003', 'default_institution', 'ASSI-STD-03', 'Historical Archived LMS & Assignments Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
