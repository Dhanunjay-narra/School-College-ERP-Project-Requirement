-- Multi-Store Warehouse Management Production Seed Data
INSERT INTO erp_warehouses_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('WARE-001', 'default_institution', 'WARE-STD-01', 'Primary Active Multi-Store Warehouse Management Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('WARE-002', 'default_institution', 'WARE-STD-02', 'Secondary Verified Multi-Store Warehouse Management Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('WARE-003', 'default_institution', 'WARE-STD-03', 'Historical Archived Multi-Store Warehouse Management Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
