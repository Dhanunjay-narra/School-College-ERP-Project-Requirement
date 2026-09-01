-- Campus Inventory & Stores Production Seed Data
INSERT INTO erp_inventory_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('INVE-001', 'default_institution', 'INVE-STD-01', 'Primary Active Campus Inventory & Stores Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('INVE-002', 'default_institution', 'INVE-STD-02', 'Secondary Verified Campus Inventory & Stores Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('INVE-003', 'default_institution', 'INVE-STD-03', 'Historical Archived Campus Inventory & Stores Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
