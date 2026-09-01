-- Fees & Student Billing Extended Seed Entries
INSERT INTO erp_fees_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('FEES-EXT-01', 'default_institution', 'FEES-EXT-1', 'Extended Fees & Student Billing Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('FEES-EXT-02', 'default_institution', 'FEES-EXT-2', 'Extended Fees & Student Billing Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
