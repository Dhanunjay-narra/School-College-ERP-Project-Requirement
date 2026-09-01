-- Identity & Access Management Extended Seed Entries
INSERT INTO erp_identity_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('IDEN-EXT-01', 'default_institution', 'IDEN-EXT-1', 'Extended Identity & Access Management Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('IDEN-EXT-02', 'default_institution', 'IDEN-EXT-2', 'Extended Identity & Access Management Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
