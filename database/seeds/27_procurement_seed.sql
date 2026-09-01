-- Procurement Management Production Seed Data
INSERT INTO erp_procurement_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PROC-001', 'default_institution', 'PROC-STD-01', 'Primary Active Procurement Management Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PROC-002', 'default_institution', 'PROC-STD-02', 'Secondary Verified Procurement Management Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PROC-003', 'default_institution', 'PROC-STD-03', 'Historical Archived Procurement Management Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
