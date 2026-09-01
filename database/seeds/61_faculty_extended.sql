-- Faculty & Workload Management Extended Seed Entries
INSERT INTO erp_faculty_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('FACU-EXT-01', 'default_institution', 'FACU-EXT-1', 'Extended Faculty & Workload Management Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('FACU-EXT-02', 'default_institution', 'FACU-EXT-2', 'Extended Faculty & Workload Management Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
