-- Campus Inventory & Stores Extended Seed Entries
INSERT INTO erp_inventory_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('INVE-EXT-01', 'default_institution', 'INVE-EXT-1', 'Extended Campus Inventory & Stores Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('INVE-EXT-02', 'default_institution', 'INVE-EXT-2', 'Extended Campus Inventory & Stores Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
