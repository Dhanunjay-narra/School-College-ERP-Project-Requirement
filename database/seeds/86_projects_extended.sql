-- Campus Infrastructure Projects Extended Seed Entries
INSERT INTO erp_projects_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PROJ-EXT-01', 'default_institution', 'PROJ-EXT-1', 'Extended Campus Infrastructure Projects Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PROJ-EXT-02', 'default_institution', 'PROJ-EXT-2', 'Extended Campus Infrastructure Projects Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
