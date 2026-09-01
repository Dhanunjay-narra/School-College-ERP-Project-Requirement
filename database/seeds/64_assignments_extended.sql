-- LMS & Assignments Extended Seed Entries
INSERT INTO erp_assignments_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ASSI-EXT-01', 'default_institution', 'ASSI-EXT-1', 'Extended LMS & Assignments Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ASSI-EXT-02', 'default_institution', 'ASSI-EXT-2', 'Extended LMS & Assignments Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
