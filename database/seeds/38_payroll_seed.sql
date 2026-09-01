-- Integrated Payroll Engine Production Seed Data
INSERT INTO erp_payroll_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PAYR-001', 'default_institution', 'PAYR-STD-01', 'Primary Active Integrated Payroll Engine Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PAYR-002', 'default_institution', 'PAYR-STD-02', 'Secondary Verified Integrated Payroll Engine Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PAYR-003', 'default_institution', 'PAYR-STD-03', 'Historical Archived Integrated Payroll Engine Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
