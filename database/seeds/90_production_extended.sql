-- Campus Workshop & Fab Lab Extended Seed Entries
INSERT INTO erp_production_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PROD-EXT-01', 'default_institution', 'PROD-EXT-1', 'Extended Campus Workshop & Fab Lab Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PROD-EXT-02', 'default_institution', 'PROD-EXT-2', 'Extended Campus Workshop & Fab Lab Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
