-- Immutable Audit Logging Extended Seed Entries
INSERT INTO erp_audit_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('AUDI-EXT-01', 'default_institution', 'AUDI-EXT-1', 'Extended Immutable Audit Logging Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('AUDI-EXT-02', 'default_institution', 'AUDI-EXT-2', 'Extended Immutable Audit Logging Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
