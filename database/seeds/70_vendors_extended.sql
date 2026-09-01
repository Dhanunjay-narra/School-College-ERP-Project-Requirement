-- Vendor Management & Compliance Extended Seed Entries
INSERT INTO erp_vendors_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('VEND-EXT-01', 'default_institution', 'VEND-EXT-1', 'Extended Vendor Management & Compliance Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('VEND-EXT-02', 'default_institution', 'VEND-EXT-2', 'Extended Vendor Management & Compliance Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
