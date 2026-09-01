-- Fees & Student Billing Production Seed Data
INSERT INTO erp_fees_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('FEES-001', 'default_institution', 'FEES-STD-01', 'Primary Active Fees & Student Billing Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('FEES-002', 'default_institution', 'FEES-STD-02', 'Secondary Verified Fees & Student Billing Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('FEES-003', 'default_institution', 'FEES-STD-03', 'Historical Archived Fees & Student Billing Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
