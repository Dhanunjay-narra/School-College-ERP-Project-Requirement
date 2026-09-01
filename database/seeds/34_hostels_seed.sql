-- Hostel & Housing Management Production Seed Data
INSERT INTO erp_hostels_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('HOST-001', 'default_institution', 'HOST-STD-01', 'Primary Active Hostel & Housing Management Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('HOST-002', 'default_institution', 'HOST-STD-02', 'Secondary Verified Hostel & Housing Management Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('HOST-003', 'default_institution', 'HOST-STD-03', 'Historical Archived Hostel & Housing Management Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
