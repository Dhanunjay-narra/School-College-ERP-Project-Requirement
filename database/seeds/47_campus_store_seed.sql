-- Campus Store & Cafeteria POS Production Seed Data
INSERT INTO erp_campus_store_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('CAMP-001', 'default_institution', 'CAMP-STD-01', 'Primary Active Campus Store & Cafeteria POS Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('CAMP-002', 'default_institution', 'CAMP-STD-02', 'Secondary Verified Campus Store & Cafeteria POS Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('CAMP-003', 'default_institution', 'CAMP-STD-03', 'Historical Archived Campus Store & Cafeteria POS Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
