-- Transportation & GPS Fleet Production Seed Data
INSERT INTO erp_transport_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('TRAN-001', 'default_institution', 'TRAN-STD-01', 'Primary Active Transportation & GPS Fleet Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('TRAN-002', 'default_institution', 'TRAN-STD-02', 'Secondary Verified Transportation & GPS Fleet Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('TRAN-003', 'default_institution', 'TRAN-STD-03', 'Historical Archived Transportation & GPS Fleet Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
