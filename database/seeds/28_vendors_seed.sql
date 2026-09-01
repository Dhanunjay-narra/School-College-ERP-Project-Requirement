-- Vendor Management & Compliance Production Seed Data
INSERT INTO erp_vendors_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('VEND-001', 'default_institution', 'VEND-STD-01', 'Primary Active Vendor Management & Compliance Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('VEND-002', 'default_institution', 'VEND-STD-02', 'Secondary Verified Vendor Management & Compliance Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('VEND-003', 'default_institution', 'VEND-STD-03', 'Historical Archived Vendor Management & Compliance Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
