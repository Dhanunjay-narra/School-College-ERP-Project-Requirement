-- Asset Lifecycle & Depreciation Production Seed Data
INSERT INTO erp_assets_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ASSE-001', 'default_institution', 'ASSE-STD-01', 'Primary Active Asset Lifecycle & Depreciation Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ASSE-002', 'default_institution', 'ASSE-STD-02', 'Secondary Verified Asset Lifecycle & Depreciation Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ASSE-003', 'default_institution', 'ASSE-STD-03', 'Historical Archived Asset Lifecycle & Depreciation Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
