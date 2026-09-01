-- Accounts Payable & Receivable Extended Seed Entries
INSERT INTO erp_accounting_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('ACCO-EXT-01', 'default_institution', 'ACCO-EXT-1', 'Extended Accounts Payable & Receivable Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('ACCO-EXT-02', 'default_institution', 'ACCO-EXT-2', 'Extended Accounts Payable & Receivable Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
