-- Examinations & Grading Production Seed Data
INSERT INTO erp_examinations_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('EXAM-001', 'default_institution', 'EXAM-STD-01', 'Primary Active Examinations & Grading Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('EXAM-002', 'default_institution', 'EXAM-STD-02', 'Secondary Verified Examinations & Grading Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('EXAM-003', 'default_institution', 'EXAM-STD-03', 'Historical Archived Examinations & Grading Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
