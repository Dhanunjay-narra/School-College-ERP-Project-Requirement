-- Applicant Tracking System Extended Seed Entries
INSERT INTO erp_recruitment_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('RECR-EXT-01', 'default_institution', 'RECR-EXT-1', 'Extended Applicant Tracking System Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('RECR-EXT-02', 'default_institution', 'RECR-EXT-2', 'Extended Applicant Tracking System Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
