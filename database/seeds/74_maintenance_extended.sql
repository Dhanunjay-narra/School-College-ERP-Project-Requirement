-- Campus Facility Maintenance Extended Seed Entries
INSERT INTO erp_maintenance_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('MAIN-EXT-01', 'default_institution', 'MAIN-EXT-1', 'Extended Campus Facility Maintenance Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('MAIN-EXT-02', 'default_institution', 'MAIN-EXT-2', 'Extended Campus Facility Maintenance Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
