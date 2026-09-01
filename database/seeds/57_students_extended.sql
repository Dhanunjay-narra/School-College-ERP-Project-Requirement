-- Student Information & Lifecycle Extended Seed Entries
INSERT INTO erp_students_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('STUD-EXT-01', 'default_institution', 'STUD-EXT-1', 'Extended Student Information & Lifecycle Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('STUD-EXT-02', 'default_institution', 'STUD-EXT-2', 'Extended Student Information & Lifecycle Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
