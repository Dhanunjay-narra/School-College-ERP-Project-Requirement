-- Asset Lifecycle & Depreciation Extended Seed Entries
INSERT INTO erp_assets_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ASSE-EXT-01', 'default_institution', 'ASSE-EXT-1', 'Extended Asset Lifecycle & Depreciation Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ASSE-EXT-02', 'default_institution', 'ASSE-EXT-2', 'Extended Asset Lifecycle & Depreciation Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
