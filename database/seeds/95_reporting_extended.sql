-- Universal Enterprise Reporting Extended Seed Entries
INSERT INTO erp_reporting_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('REPO-EXT-01', 'default_institution', 'REPO-EXT-1', 'Extended Universal Enterprise Reporting Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('REPO-EXT-02', 'default_institution', 'REPO-EXT-2', 'Extended Universal Enterprise Reporting Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
