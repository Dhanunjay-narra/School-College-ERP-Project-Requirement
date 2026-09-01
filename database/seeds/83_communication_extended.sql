-- Universal Multi-Channel Notifications Extended Seed Entries
INSERT INTO erp_communication_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('COMM-EXT-01', 'default_institution', 'COMM-EXT-1', 'Extended Universal Multi-Channel Notifications Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('COMM-EXT-02', 'default_institution', 'COMM-EXT-2', 'Extended Universal Multi-Channel Notifications Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
