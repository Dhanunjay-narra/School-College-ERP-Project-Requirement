-- Transportation & GPS Fleet Extended Seed Entries
INSERT INTO erp_transport_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('TRAN-EXT-01', 'default_institution', 'TRAN-EXT-1', 'Extended Transportation & GPS Fleet Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('TRAN-EXT-02', 'default_institution', 'TRAN-EXT-2', 'Extended Transportation & GPS Fleet Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
