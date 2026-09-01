-- Hostel & Housing Management Extended Seed Entries
INSERT INTO erp_hostels_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('HOST-EXT-01', 'default_institution', 'HOST-EXT-1', 'Extended Hostel & Housing Management Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('HOST-EXT-02', 'default_institution', 'HOST-EXT-2', 'Extended Hostel & Housing Management Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
