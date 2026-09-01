-- Research & Innovation Management Production Seed Data
INSERT INTO erp_research_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('RESE-001', 'default_institution', 'RESE-STD-01', 'Primary Active Research & Innovation Management Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('RESE-002', 'default_institution', 'RESE-STD-02', 'Secondary Verified Research & Innovation Management Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('RESE-003', 'default_institution', 'RESE-STD-03', 'Historical Archived Research & Innovation Management Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
