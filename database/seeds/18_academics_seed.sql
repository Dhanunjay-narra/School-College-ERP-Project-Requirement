-- Academic Structure & Timetable Production Seed Data
INSERT INTO erp_academics_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ACAD-001', 'default_institution', 'ACAD-STD-01', 'Primary Active Academic Structure & Timetable Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ACAD-002', 'default_institution', 'ACAD-STD-02', 'Secondary Verified Academic Structure & Timetable Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ACAD-003', 'default_institution', 'ACAD-STD-03', 'Historical Archived Academic Structure & Timetable Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
