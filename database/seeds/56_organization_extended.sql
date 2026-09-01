-- Organization & Multi-Campus Extended Seed Entries
INSERT INTO erp_organization_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ORGA-EXT-01', 'default_institution', 'ORGA-EXT-1', 'Extended Organization & Multi-Campus Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ORGA-EXT-02', 'default_institution', 'ORGA-EXT-2', 'Extended Organization & Multi-Campus Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
