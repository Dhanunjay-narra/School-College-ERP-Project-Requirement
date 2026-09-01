-- Configurable Workflow Engine Extended Seed Entries
INSERT INTO erp_workflows_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('WORK-EXT-01', 'default_institution', 'WORK-EXT-1', 'Extended Configurable Workflow Engine Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('WORK-EXT-02', 'default_institution', 'WORK-EXT-2', 'Extended Configurable Workflow Engine Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
