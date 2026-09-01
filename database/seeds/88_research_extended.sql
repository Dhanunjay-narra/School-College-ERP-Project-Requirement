-- Research & Innovation Management Extended Seed Entries
INSERT INTO erp_research_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('RESE-EXT-01', 'default_institution', 'RESE-EXT-1', 'Extended Research & Innovation Management Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('RESE-EXT-02', 'default_institution', 'RESE-EXT-2', 'Extended Research & Innovation Management Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
