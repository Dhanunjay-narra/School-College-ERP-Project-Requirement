-- Payment Abstraction Gateway Extended Seed Entries
INSERT INTO erp_payments_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PAYM-EXT-01', 'default_institution', 'PAYM-EXT-1', 'Extended Payment Abstraction Gateway Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PAYM-EXT-02', 'default_institution', 'PAYM-EXT-2', 'Extended Payment Abstraction Gateway Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
