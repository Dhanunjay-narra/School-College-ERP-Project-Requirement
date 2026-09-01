-- Integrated Payroll Engine Extended Seed Entries
INSERT INTO erp_payroll_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PAYR-EXT-01', 'default_institution', 'PAYR-EXT-1', 'Extended Integrated Payroll Engine Analytics Sample', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PAYR-EXT-02', 'default_institution', 'PAYR-EXT-2', 'Extended Integrated Payroll Engine Telemetry Dataset', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
