-- Smart Attendance Engine Extended Seed Entries
INSERT INTO erp_attendance_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ATTE-EXT-01', 'default_institution', 'ATTE-EXT-1', 'Extended Smart Attendance Engine Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ATTE-EXT-02', 'default_institution', 'ATTE-EXT-2', 'Extended Smart Attendance Engine Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
