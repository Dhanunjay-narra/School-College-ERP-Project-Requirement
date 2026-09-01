-- Human Resource & Recruitment Extended Seed Entries
INSERT INTO erp_hr_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('HR-EXT-01', 'default_institution', 'HR-EXT-1', 'Extended Human Resource & Recruitment Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('HR-EXT-02', 'default_institution', 'HR-EXT-2', 'Extended Human Resource & Recruitment Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
