-- Multi-Store Warehouse Management Extended Seed Entries
INSERT INTO erp_warehouses_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('WARE-EXT-01', 'default_institution', 'WARE-EXT-1', 'Extended Multi-Store Warehouse Management Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('WARE-EXT-02', 'default_institution', 'WARE-EXT-2', 'Extended Multi-Store Warehouse Management Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
