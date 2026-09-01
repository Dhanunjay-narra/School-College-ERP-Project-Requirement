-- Alumni Network & Relations Extended Seed Entries
INSERT INTO erp_alumni_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ALUM-EXT-01', 'default_institution', 'ALUM-EXT-1', 'Extended Alumni Network & Relations Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ALUM-EXT-02', 'default_institution', 'ALUM-EXT-2', 'Extended Alumni Network & Relations Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
