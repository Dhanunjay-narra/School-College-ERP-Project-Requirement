-- Campus Store & Cafeteria POS Extended Seed Entries
INSERT INTO erp_campus_store_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('CAMP-EXT-01', 'default_institution', 'CAMP-EXT-1', 'Extended Campus Store & Cafeteria POS Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('CAMP-EXT-02', 'default_institution', 'CAMP-EXT-2', 'Extended Campus Store & Cafeteria POS Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
