-- Finance & General Ledger Extended Seed Entries
INSERT INTO erp_finance_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('FINA-EXT-01', 'default_institution', 'FINA-EXT-1', 'Extended Finance & General Ledger Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('FINA-EXT-02', 'default_institution', 'FINA-EXT-2', 'Extended Finance & General Ledger Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
