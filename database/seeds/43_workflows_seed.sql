-- Configurable Workflow Engine Production Seed Data
INSERT INTO erp_workflows_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('WORK-001', 'default_institution', 'WORK-STD-01', 'Primary Active Configurable Workflow Engine Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('WORK-002', 'default_institution', 'WORK-STD-02', 'Secondary Verified Configurable Workflow Engine Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('WORK-003', 'default_institution', 'WORK-STD-03', 'Historical Archived Configurable Workflow Engine Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
