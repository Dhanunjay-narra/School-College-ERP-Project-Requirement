-- Centralized Faceted Search Extended Seed Entries
INSERT INTO erp_search_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('SEAR-EXT-01', 'default_institution', 'SEAR-EXT-1', 'Extended Centralized Faceted Search Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('SEAR-EXT-02', 'default_institution', 'SEAR-EXT-2', 'Extended Centralized Faceted Search Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
