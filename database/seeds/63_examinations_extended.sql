-- Examinations & Grading Extended Seed Entries
INSERT INTO erp_examinations_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('EXAM-EXT-01', 'default_institution', 'EXAM-EXT-1', 'Extended Examinations & Grading Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('EXAM-EXT-02', 'default_institution', 'EXAM-EXT-2', 'Extended Examinations & Grading Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
