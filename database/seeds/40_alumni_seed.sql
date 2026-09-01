-- Alumni Network & Relations Production Seed Data
INSERT INTO erp_alumni_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ALUM-001', 'default_institution', 'ALUM-STD-01', 'Primary Active Alumni Network & Relations Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ALUM-002', 'default_institution', 'ALUM-STD-02', 'Secondary Verified Alumni Network & Relations Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ALUM-003', 'default_institution', 'ALUM-STD-03', 'Historical Archived Alumni Network & Relations Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
