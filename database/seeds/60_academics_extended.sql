-- Academic Structure & Timetable Extended Seed Entries
INSERT INTO erp_academics_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ACAD-EXT-01', 'default_institution', 'ACAD-EXT-1', 'Extended Academic Structure & Timetable Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ACAD-EXT-02', 'default_institution', 'ACAD-EXT-2', 'Extended Academic Structure & Timetable Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
