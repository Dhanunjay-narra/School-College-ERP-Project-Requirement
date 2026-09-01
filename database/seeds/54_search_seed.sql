-- Centralized Faceted Search Production Seed Data
INSERT INTO erp_search_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('SEAR-001', 'default_institution', 'SEAR-STD-01', 'Primary Active Centralized Faceted Search Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('SEAR-002', 'default_institution', 'SEAR-STD-02', 'Secondary Verified Centralized Faceted Search Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('SEAR-003', 'default_institution', 'SEAR-STD-03', 'Historical Archived Centralized Faceted Search Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
