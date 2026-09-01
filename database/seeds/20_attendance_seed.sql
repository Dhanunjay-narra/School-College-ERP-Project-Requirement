-- Smart Attendance Engine Production Seed Data
INSERT INTO erp_attendance_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ATTE-001', 'default_institution', 'ATTE-STD-01', 'Primary Active Smart Attendance Engine Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ATTE-002', 'default_institution', 'ATTE-STD-02', 'Secondary Verified Smart Attendance Engine Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ATTE-003', 'default_institution', 'ATTE-STD-03', 'Historical Archived Smart Attendance Engine Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
