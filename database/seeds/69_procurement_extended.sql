-- Procurement Management Extended Seed Entries
INSERT INTO erp_procurement_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PROC-EXT-01', 'default_institution', 'PROC-EXT-1', 'Extended Procurement Management Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PROC-EXT-02', 'default_institution', 'PROC-EXT-2', 'Extended Procurement Management Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
