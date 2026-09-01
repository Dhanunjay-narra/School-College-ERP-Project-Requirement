-- Applicant Tracking System Production Seed Data
INSERT INTO erp_recruitment_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('RECR-001', 'default_institution', 'RECR-STD-01', 'Primary Active Applicant Tracking System Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('RECR-002', 'default_institution', 'RECR-STD-02', 'Secondary Verified Applicant Tracking System Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('RECR-003', 'default_institution', 'RECR-STD-03', 'Historical Archived Applicant Tracking System Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
