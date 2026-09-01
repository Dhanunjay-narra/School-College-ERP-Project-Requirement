-- Accounts Payable & Receivable Production Seed Data
INSERT INTO erp_accounting_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ACCO-001', 'default_institution', 'ACCO-STD-01', 'Primary Active Accounts Payable & Receivable Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ACCO-002', 'default_institution', 'ACCO-STD-02', 'Secondary Verified Accounts Payable & Receivable Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ACCO-003', 'default_institution', 'ACCO-STD-03', 'Historical Archived Accounts Payable & Receivable Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
