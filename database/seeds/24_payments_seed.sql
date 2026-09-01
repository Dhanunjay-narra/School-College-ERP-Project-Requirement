-- Payment Abstraction Gateway Production Seed Data
INSERT INTO erp_payments_records (id, tenant_id, code, name, status, created_at, updated_at) VALUES
('PAYM-001', 'default_institution', 'PAYM-STD-01', 'Primary Active Payment Abstraction Gateway Record', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PAYM-002', 'default_institution', 'PAYM-STD-02', 'Secondary Verified Payment Abstraction Gateway Entry', 'ACTIVE', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('PAYM-003', 'default_institution', 'PAYM-STD-03', 'Historical Archived Payment Abstraction Gateway Dataset', 'ARCHIVED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
ON CONFLICT (id) DO NOTHING;
