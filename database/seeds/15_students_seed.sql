-- Student Information & Lifecycle Production Seed Data
INSERT INTO erp_students_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('STUD-001', 'default_institution', 'STUD-STD-01', 'Primary Active Student Information & Lifecycle Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('STUD-002', 'default_institution', 'STUD-STD-02', 'Secondary Verified Student Information & Lifecycle Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('STUD-003', 'default_institution', 'STUD-STD-03', 'Historical Archived Student Information & Lifecycle Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
