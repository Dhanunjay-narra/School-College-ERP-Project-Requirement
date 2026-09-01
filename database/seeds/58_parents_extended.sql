-- Parent & Guardian Management Extended Seed Entries
INSERT INTO erp_parents_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PARE-EXT-01', 'default_institution', 'PARE-EXT-1', 'Extended Parent & Guardian Management Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PARE-EXT-02', 'default_institution', 'PARE-EXT-2', 'Extended Parent & Guardian Management Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
