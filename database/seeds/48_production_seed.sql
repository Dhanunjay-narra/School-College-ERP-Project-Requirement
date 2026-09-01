-- Campus Workshop & Fab Lab Production Seed Data
INSERT INTO erp_production_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PROD-001', 'default_institution', 'PROD-STD-01', 'Primary Active Campus Workshop & Fab Lab Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PROD-002', 'default_institution', 'PROD-STD-02', 'Secondary Verified Campus Workshop & Fab Lab Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PROD-003', 'default_institution', 'PROD-STD-03', 'Historical Archived Campus Workshop & Fab Lab Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
