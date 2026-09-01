-- Finance & General Ledger Production Seed Data
INSERT INTO erp_finance_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('FINA-001', 'default_institution', 'FINA-STD-01', 'Primary Active Finance & General Ledger Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('FINA-002', 'default_institution', 'FINA-STD-02', 'Secondary Verified Finance & General Ledger Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('FINA-003', 'default_institution', 'FINA-STD-03', 'Historical Archived Finance & General Ledger Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
