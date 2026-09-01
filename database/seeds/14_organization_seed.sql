-- Organization & Multi-Campus Production Seed Data
INSERT INTO erp_organization_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ORGA-001', 'default_institution', 'ORGA-STD-01', 'Primary Active Organization & Multi-Campus Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ORGA-002', 'default_institution', 'ORGA-STD-02', 'Secondary Verified Organization & Multi-Campus Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ORGA-003', 'default_institution', 'ORGA-STD-03', 'Historical Archived Organization & Multi-Campus Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
