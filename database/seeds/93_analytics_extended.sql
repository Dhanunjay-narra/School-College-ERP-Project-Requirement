-- BI & Institutional Analytics Extended Seed Entries
INSERT INTO erp_analytics_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ANAL-EXT-01', 'default_institution', 'ANAL-EXT-1', 'Extended BI & Institutional Analytics Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ANAL-EXT-02', 'default_institution', 'ANAL-EXT-2', 'Extended BI & Institutional Analytics Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
